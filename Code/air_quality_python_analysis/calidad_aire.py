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
import pandas
import numpy

#Select data
files_url = {2014: 'https://datos.madrid.es/egob/catalogo/201200-26-calidad-aire-horario.zip',
             2015: 'https://datos.madrid.es/egob/catalogo/201200-27-calidad-aire-horario.zip',
             2016: 'https://datos.madrid.es/egob/catalogo/201200-28-calidad-aire-horario.zip',
             2017: 'https://datos.madrid.es/egob/catalogo/201200-10306313-calidad-aire-horario.zip',
             2018: 'https://datos.madrid.es/egob/catalogo/201200-10306314-calidad-aire-horario.zip'}

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


