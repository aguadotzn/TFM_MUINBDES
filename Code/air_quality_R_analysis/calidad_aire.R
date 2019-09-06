#----------------------------
#MUINBDES_TFM_CALIDAD_AIRE_MADRID
#Autor: Adrián Aguado
#Fecha: Agosto 2019
#Descripción: Preprocesado, formateado y análisis con R
#Nombre fichero: calidad_aire.R
#Fuente datos: https://datos.madrid.es/
#----------------------------
#In R is really important to set properly the path, otherwise we'll receive errors
setwd("/Users/adrianaguado/Documents/WorkspaceDataScience/TFM_MUINBDES/Code/data/hourly_data")

#LIBRARIES
# You need to install the packages in Rstudio.
# https://www.r-bloggers.com/installing-r-packages/
# If you execute any library and receive the error message "Error in library(XX): there is no package called 'XX'".
# you must first install it and then execute library(XX).
library("ggplot2")
library("tidyverse")

start.time <- Sys.time() #Measuring code execution time in R (START)
# LOAD DATA *************************************************
# List name of the files 
files <- list.files(pattern = ".*mo1[1-9].txt")

# Name of columns
columns_name <- c("estacion","contaminante","tecnica","periodo","ano","mes","dia","h1","h2","h3","h4","h5","h6","h7","h8","h9","h10","h11","h12","h13","h14","h15","h16","h17","h18","h19","h20","h21","h22","h23","h24")
contaminante = c("Dióxido de Azufre","Monóxido de Carbono","Monóxido de Nitrógeno","Dióxido de Nitrógeno","Partículas PM2.5","Partículas PM10","Óxidos de Nitrógeno","Ozono","Tolueno","Benceno","Etilbenceno","Hidrocarburos totales
(hexano)","Metano","Hidrocarburos no metánicos (hexano)")

# Width of columns
width <- c(8,2,2,2,2,2,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6)

# TRANSFORM DATA **************************************************
# Create a dataframe 
# Invalid measures ("00.00N") are overwritten with "NA".
for (file in files){
  # If the DataSet does not exist, we create it
  if (!exists("calidad_aire")){
    calidad_aire <- read.fwf(file = file, widths = width, header = FALSE, col.names = columns_name, na.strings = c("00.00N"))
    #print('Load...')
  } 
  # If the DataSet exist, we adjust the values
  if (exists("calidad_aire")){
    temp_dataset <- read.fwf(file = file, widths = width, header = FALSE, col.names = columns_name, na.strings = c("00.00N"))
    calidad_aire <- rbind(calidad_aire, temp_dataset)
    rm(temp_dataset)
    #print('Load...')
  }
}

#Delete V
for (i in 8:31) {
  calidad_aire[,i]<-gsub("V","",calidad_aire[,i])
}

# Transform the type of each columns
calidad_aire <- transform(calidad_aire, estacion=as.factor(estacion), contaminante=as.factor(contaminante), tecnica=as.factor(tecnica), periodo=as.factor(periodo), timestamp=as.Date(timestamp, format("%d/%m/%y")))
calidad_aire[,8:31] <- sapply(calidad_aire[,8:31], as.numeric)

# We create a timestamp column: dd/mm/yy
ts <- c( 'dia' , 'mes' , 'ano')
calidad_aire$timestamp <- apply(calidad_aire[ , ts ] , 1 , paste , collapse = "/")
# If we want to substitute the values of day,month,year we can use the lines below:
#calidad_aire$timestamp <- apply(calidad_aire, ano=paste(dia, mes, ano, sep="/"))
#colnames(calidad_aire)[5]<-"timestamp"
#calidad_aire<-calidad_aire[,!names(calidad_aire) %in% c("mes", "dia")]

# Columns to merge data
cols <- c( 'h1' , 'h2' , 'h3', 'h4', 'h5' , 'h6' , 'h7', 'h8', 'h9' , 'h10' , 'h11', 'h12', 'h13' , 'h14' , 'h15', 'h16', 'h17' , 'h18' , 'h19', 'h20', 'h21','h22', 'h23', 'h24')
# Create a new column with a list of the values
calidad_aire$values <- apply(calidad_aire[ , cols ] , 1 , paste , collapse = "," )

# Order by timestamp, estación y contaminante
calidad_aire <- calidad_aire[order(calidad_aire$timestamp, calidad_aire$estacion, calidad_aire$contaminante),]

# EXPORT DATA **************************************************
# If we want we can export the data just in case we want to visualize it with other tools. For instance: PowerBi 
#write.csv(calidad_aire, file = "formatted_data/calidad_aire.csv", row.names = FALSE)

# EXPLORE DATA **************************************************
colName <- names(calidad_aire) # Name of columns
rowNumber <- dim.data.frame(calidad_aire) # Number of rows 
colNumber <- dim.data.frame(calidad_aire) # Number of columns 
#cat("Num Filas   : ", rowNumber, "\nNum Columnas: ", colNumber)

# With this line we can know the type of each column. In this case we have factor, Date and numeric
#lapply(calidad_aire, class)

# We create a copy of the original file just to work with a different file
df_calidad_aire <- calidad_aire

# Summary of the data (Length, min, max, mean, median)
summary(df_calidad_aire)

# Summary of the data by each column
#str(df_calidad_aire)

# With this line we can know the number of wrong measures per column
#na_count <- sapply(calidad_aire, function(y) sum(is.na(y)))

# With this lines we can review the columns and see the (different) values
#levels(df_calidad_aire$estacion)
#levels(df_calidad_aire$contaminante)
#levels(df_calidad_aire$tecnica)

# See the first 20 lines
# head(df_calidad_aire, n=20)

# VISUALIZE DATA ***********************************************
# Some examples of visualizations

# Boxplot. In this case for Contaminante = 8 (NO2)
j=1
for (i in levels(df_calidad_aire$contaminante==8)){
  print(df_calidad_aire$contaminante)
  boxplot(df_calidad_aire[df_calidad_aire$contaminante==8,8:31], main=contaminante[j], outline = FALSE)
  j=j+1
}

# ggplot. We  calculate here the worst hours per year. Notice hx correspond with the hour
ggplot(data = df_calidad_aire) +
  xlab("Year") +
  ylab("Total value per hour") +
  scale_y_continuous(limits=c(0,max(df_calidad_aire$h2,na.rm=TRUE))) +  
  geom_bar(mapping = aes(x = ano, y = h1), stat = "identity")

# ggplot. We calculate here, at 8:00, the worst months. Notice hx correspond with the hour.
ggplot(data = df_calidad_aire) +
  #filter( df_calidad_aire$contaminante==8 ) %>%
  xlab("Month") +
  ylab("Total value") +
  stat_summary(
    mapping = aes(x = mes, y = h8),
    fun.ymin = min,
    fun.ymax = max,
    fun.y = median
  )

# ggplot. Experimenting with anual values 
anual_limit<- 40
ggplot(df_calidad_aire,aes(x=ano,y=values,color=values)) +
  geom_point() +
  theme(axis.text.x =element_text(angle=0)) +
  ggtitle("Gráfico de NO2") +
  xlab(label="YEar") +
  ylab(label="NO2 value") + 
  geom_hline(yintercept = anual_limit)



#Measuring code execution time in R (END)
end.time <- Sys.time()
time.taken <- end.time - start.time
#time.taken




