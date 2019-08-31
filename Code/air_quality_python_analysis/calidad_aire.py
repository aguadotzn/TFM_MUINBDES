#!/usr/bin/python
#MUINBDES_TFM_CALIDAD_AIRE_MADRID
# -------------------------------------------------
# Autor: Adrian Aguado
#
# Fecha: Julio 2019
#
# Nombre fichero: calidad_aire
#
# Fuente datos: https://datos.madrid.es/
# -------------------------------------------------

#Load libraries
import urllib
import zipfile
import tempfile
import pandas
import numpy


#Select data
files_url = {2014: 'https://datos.madrid.es/egob/catalogo/201200-26-calidad-aire-horario.zip',
             2015: 'https://datos.madrid.es/egob/catalogo/201200-27-calidad-aire-horario.zip',
             2016: 'https://datos.madrid.es/egob/catalogo/201200-28-calidad-aire-horario.zip',
             2017: 'https://datos.madrid.es/egob/catalogo/201200-10306313-calidad-aire-horario.zip',
             2018: 'https://datos.madrid.es/egob/catalogo/201200-10306314-calidad-aire-horario.zip'}

#Magnitudes
mapper_magnitudes = {1: 'SO2',
                     6: 'CO',
                     7: 'NO',
                     8: 'NO2',
                     9: 'PM2.5u',
                     10: 'PM10u',
                     12: 'NOX',
                     14: 'O3',
                     20: 'Tolueno',
                     30: 'Benceno',
                     35: 'Etilbenceno',
                     37: 'Metaxileno',
                     38: 'Paraxileno',
                     39: 'Ortoxileno',
                     42: 'hidrocarburos',
                     43: 'CH4',
                     44: 'Hidrocarburnos no metanicos'}


#Function to read txt
def read_txt_format(file):
    df = list()
    for line in file:
        line_str = line.decode("utf-8").replace(',', '')

        try:
            data = {'PROVINCIA': int(line_str[0:2]),
                    'MUNICIPIO': int(line_str[2:5]),
                    'ESTACION': int(line_str[5:8]),
                    'MAGNITUD': int(line_str[8:10]),
                    'PUNTO_MUESTREO': str(line_str[0:8]) + '_' + \
                                      str(int(line_str[8:10])) + '_' + str(line_str[10:12]),
                    'ANO': int(line_str[14:16]),
                    'MES': int(line_str[16:18]),
                    'DIA': int(line_str[18:20])}

            for h in range(24):
                ch = 'H{0:02}'.format(h + 1)
                hv = float(line_str[20 + h * 6:25 + h * 6])
                data[ch] = hv

                ch = 'V{0:02}'.format(h + 1)
                hv = line_str[25 + h * 6]
                data[ch] = hv
        except:
            # If fails, it is because a wrong format of txt. We need to reload data and jump 12-15 chars
            try:
                data = {'PROVINCIA': int(line_str[0:2]),
                        'MUNICIPIO': int(line_str[2:5]),
                        'ESTACION': int(line_str[5:8]),
                        'MAGNITUD': int(line_str[8:10]),
                        'PUNTO_MUESTREO': str(line_str[0:8]) + '_' + \
                                          str(int(line_str[8:10])) + '_' + str(line_str[10:12]),
                        'ANO': int(line_str[16:18]),
                        'MES': int(line_str[18:20]),
                        'DIA': int(line_str[20:22])}

                for h in range(24):
                    ch = 'H{0:02}'.format(h + 1)
                    hv = float(line_str[22 + h * 6:27 + h * 6])
                    data[ch] = hv

                    ch = 'V{0:02}'.format(h + 1)
                    hv = line_str[27 + h * 6]
                    data[ch] = hv
            except:
                print(line_str)
                for p, v in data.items():
                    print(p, v)
                raise ()

        df.append(data)
    df = pandas.DataFrame(df)
    return df

# We merge data from data control stations just to create a unique csv
df_estaciones = pandas.read_csv('../air_quality_stations/formatted_data/calidad_aire_estaciones_formatted.csv')

#Rename columns from control stations just fro simplicity
df_estaciones.rename(columns={'estacion':'descripcion'}, inplace=True)
df_estaciones.rename(columns={'numero':'estacion'}, inplace=True)
df_estaciones.rename(columns={'latitud_new':'latitud','longitud_new':'longitud'}, inplace=True)

#Establish by zonas
zonas = ['interior M30', 'sureste', 'noreste', 'noroeste', 'suroeste']
mapper_zonas = {'Escuelas Aguirre': 1,
                'Castellana': 1,
                'Plaza Castilla': 1,
                'Avda. Ramon y Cajal': 1,
                'Cuatro Caminos': 1,
                'Pza. de Espana': 1,
                'Barrio del Pilar': 1,

                'Pza. del Carmen': 1,
                'Mendez Alvaro': 1,
                'Parque del Retiro': 1,

                'Moratalaz': 2,
                'Vallecas': 2,
                'Ensanche de Vallecas': 2,

                'Arturo Soria': 3,
                'Sanchinarro': 3,
                'Urb. Embajada': 3,
                'Barajas Pueblo': 3,
                'Tres Olivos': 3,
                'Juan Carlos I': 3,

                'El Pardo': 4,
                'Casa de Campo': 4,

                'Pza. Fernandez Ladreda': 5,
                'Farolillo': 5,
                'Villaverde': 5,
                }

df_estaciones['zona'] = ''
for d in df_estaciones.descripcion.unique():
    df_estaciones.loc[df_estaciones.descripcion == d,'zona'] = zonas[mapper_zonas[d]-1]

#Transform into a list
alldf = list()

# Iterate over year-zip-files
for year, file_url in files_url.items():

    # Download zip in temp folder
    with tempfile.NamedTemporaryFile() as f:
        urllib.request.urlretrieve(file_url, f.name)

        # Open Zip
        with zipfile.ZipFile(f.name) as thezip:

            # For each file, we load the file, process it and save it correctly
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as file:

                    df = None

                    # Read CSV file
                    if zipinfo.filename[-4::] == '.csv':
                        print('Reading', zipinfo.filename)
                        df = pandas.read_csv(file, sep=';')

                    if zipinfo.filename[-4::] == '.txt':
                        print('Reading', zipinfo.filename)
                        df = read_txt_format(file)

                    if df is not None:

                        # Delete duplicates
                        df = df.drop_duplicates()

                        # Set the year
                        df.ANO = year

                        # Change column name
                        df.columns = [bytes(c.lower(), 'utf-8').decode('utf-8', 'ignore') for c in df.columns]

                        # Delete unused columns
                        df = df.drop(columns=['provincia', 'municipio', 'punto_muestreo'])

                        # Unpivot measurements
                        alldf = list()
                        for magnitud in df.magnitud.unique():
                            print(mapper_magnitudes[magnitud])
                            dfx = df[df.magnitud == magnitud]
                            ndf = list()
                            for i, row in dfx.iterrows():
                                for hora in range(24):
                                    timestamp = pandas.to_datetime(str((row.ano * 10000 + row.mes * 100 + row.dia)) + \
                                                                   '{0:02}'.format(hora), format='%Y%m%d%H')
                                    ndf.append({
                                        'estacion': row.estacion,
                                        'timestamp': timestamp,
                                        mapper_magnitudes[magnitud]: row['h{0:02}'.format(hora + 1)] \
                                                                     if row['v{0:02}'.format(hora + 1)] == 'V' \
                                                                     else numpy.nan
                                    })
                            df_magnitud = pandas.DataFrame(ndf)
                            alldf.append(df_magnitud)

                        # Merge magnitude data
                        df = alldf[0]
                        for dfx in alldf[1::]:
                            df = pandas.merge(df, dfx, on=['estacion', 'timestamp'], how='outer')

                        # Merge position data
                        df = pandas.merge(df, df_estaciones[['estacion',
                                                             'descripcion',
                                                             'altitud',
                                                             'latitud',
                                                             'longitud',
                                                             'coordinates']],
                                          on='estacion',
                                          how='left')
                        df.set_index('timestamp', inplace=True)

                        # Save data
                        df.to_csv('formatted_data/calidad_aire_{0}_{1}.csv'.format(year, zipinfo.filename), index=True)
                        alldf.append(df)

df = pandas.concat(alldf)
#Extract
df.to_csv('formatted_data/calidad_aire.csv', index=True)