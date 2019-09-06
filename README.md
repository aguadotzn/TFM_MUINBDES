# TFM_MUINBDES [![License](https://img.shields.io/cocoapods/l/ParticlesLoadingView.svg?style=flat)](LICENSE.md)
Final thesis of my Master's degree ([Business Intelligence and Big Data in Cyber-Secure Environments](https://www.inf.uva.es/master-online/))

<p align="center">
  <img width="100" height="180" src="https://upload.wikimedia.org/wikipedia/en/7/7b/University_of_Burgos_CoA.png">
  <img width="140" height="160" src="https://mir-s3-cdn-cf.behance.net/project_modules/disp/43d9f319950577.562e303b26265.gif">
  <img width="100" height="180" src="https://www.unileon.es/files/images/ule_color.preview.gif">
</p>

# Content
- [Description](https://github.com/aguadotzn/TFM_MUINBDES#Description)
- [Main process schema](https://github.com/aguadotzn/TFM_MUINBDES#Main-process-schema)
- [Data sources](https://github.com/aguadotzn/TFM_MUINBDES#Data-sources)
- [Technologies](https://github.com/aguadotzn/TFM_MUINBDES#Technologies)
- [Folders structure](https://github.com/aguadotzn/TFM_MUINBDES#Folders-structure)
- [Previews](https://github.com/aguadotzn/TFM_MUINBDES#Previews)
  - [Map](https://github.com/aguadotzn/TFM_MUINBDES#Madrid-control-station-location)
  - [NO2 2018 average](https://github.com/aguadotzn/TFM_MUINBDES#NO2-average-for-2018)
- [License](https://github.com/aguadotzn/TFM_MUINBDES#license)
- [Author](https://github.com/aguadotzn/TFM_MUINBDES#Author)



## Description
Development of an environment model for the analysis of air pollution/air quality levels in Madrid, which allows information to be better exploited by control stations distributed in different parts of the city. Both the ingestion, processing, exploitation and visualization of the data are contemplated, to answer analytical questions on the selected subject. 


## Main process schema

![Schema](/Documentation/images/diagramtech.png)

## Data sources
* Main data source: [datos.madrid](http://datos.madrid.es.)

## Technologies
* Data preparation, cleaning, and transformation
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [R](https://en.wikipedia.org/wiki/R_(programming_language))
  * [Jupyter notebooks](https://jupyter.org)
  
* Main visualization
  * [Power BI](https://powerbi.microsoft.com/)
  
* Other used tools
  * [Vega](http://vega.github.io)
  * [DataWrapper](https://www.datawrapper.de/)
  * [Tinybird](https://tinybird.co/)

## Folders structure

```

└───|- /Code
│        └─── /data
│          └─── /daily_data
│          └─── /hourly_data
│          └─── /control_stations_data
│
│        └─── /air_quality_stations
│          └─── /formatted_data
│          |-- calidad_aire_estaciones.ipynb
│
│        └─── /air_quality_python_analysis 
│          └─── /formatted_data
│          |-- calidad_aire.py
│          |-- merge_data_calidad_aire.ipynb
│
│        └─── /air_quality_R_analysis
│          └─── /formatted_data
│          |-- calidad_aire.R
│ 
│        └─── /extra
│
│        |-- README.md (code)
│ 
└───|- /Data Visualization
│        └─── /Random examples
│
│        └─── /PowerBi
│          |-- calidad_aire.pbix
│
│        |-- README.md (data visualization)
│ 
└───|- /Documentation
│        └─── /latex
│        └─── /slides (presentation)
│        └─── /images (for the main README)
│
│        |-- README.md (documentation)
│ 
└───|- /Information
│        └─── /Official Documents
│        └─── /Other Documents
│
│        |-- README.md (information)
│ 
└───|- /docs
│        └─── /assets
│        └─── /images
│
│        |-- index.html 
│        |-- README.md (github pages/landing page with some results)
│     
│-- LICENSE.md
│-- README.md (main)
```

# Previews

### _Madrid control stations location_
![Schema](/Documentation/images/cartoDBestaciones.png)
You can interact with the map [here](https://aguadotzn.carto.com/builder/7a6bc6ca-594c-44ad-8bbe-add7757e0f0d/embed). 


### _NO2 average for 2018_
![Schema](/Documentation/images/avg2018.gif)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2019 Adrián.

## Author

[Adrián Aguado](https://www.aguadotzn.com) - feel free to contact me!
