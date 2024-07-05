# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:47:19 2024

@author: enric
"""

import os
import pandas as pd
import geopandas as gpd
import numpy as np

"""
Modificar en la ruta del archivo TRI por CEB para el calculo para trigo
"""


# Lista de rutas a los archivos Shapefile
shapefile_paths_21 = [
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_21\\SHAPE\\s1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_21\\SHAPE\\G1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_21\\SHAPE\\G15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_21\\SHAPE\\G25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G1LsA\\G1L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G1LsA\\G1L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G1LsA\\G1L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G15Ls\\G15L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G15Ls\\G15L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G15Ls\\G15L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G25Ls\\G25L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G25Ls\\G25L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_21\\G25Ls\\G25L25_SAMPLED.shp",
]

shapefile_paths_22 = [
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_22\\SHAPE\\s1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_22\\SHAPE\\G1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_22\\SHAPE\\G15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_TRI_22\\SHAPE\\G25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G1LsA\\G1L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G1LsA\\G1L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G1LsA\\G1L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G15Ls\\G15L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G15Ls\\G15L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G15Ls\\G15L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G25Ls\\G25L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G25Ls\\G25L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_TRI_22\\G25Ls\\G25L25_SAMPLED.shp",
]

# Lista de nombres de las variables de interés en cada archivo
variables_21 = ['s1_1', 'G1_1', 'G15_1', 'G25_1', 'G1L1_1', 'G1L15_1', 'rvalue_1', 
             'G1L1_1', 'G1L15_1', 'rvalue_1', 'G1L1_1', 'G1L15_1', 'rvalue_1']
variables_22 = ['s1_1', 'G1_1', 'G15_1', 'G25_1', 'G1L1_1', 'G1L15_1', 'rvalue_1', 
             'G1L1_1', 'G1L15_1', 'rvalue_1', 'G1L1_1', 'G1L15_1', 'rvalue_1']

# Función para extraer el nombre de la variable desde el path
def extract_variable_name(path):
    return os.path.basename(path).split('_')[0]

# Función para cargar y combinar datos de shapefiles
def load_shapefiles(shapefile_paths, variables):
    data_frames = []
    for path, variable in zip(shapefile_paths, variables):
        gdf = gpd.read_file(path)
        gdf = gdf[['geometry', variable]].rename(columns={variable: 'value'})
        gdf['variable'] = extract_variable_name(path)
        data_frames.append(gdf)
    combined_df = pd.concat(data_frames, ignore_index=True)
    return combined_df

# Cargar los datos de ambos años
data_21 = load_shapefiles(shapefile_paths_21, variables_21)
data_22 = load_shapefiles(shapefile_paths_22, variables_22)

# Combinar los datos de ambos años
combined_data = pd.concat([data_21, data_22], ignore_index=True)

# Añadir columna de rangos
combined_data['range'] = pd.cut(combined_data['value'], bins=np.arange(0, 10500, 500))

# Calcular el coeficiente de variación por rango y variable
cv_results = combined_data.groupby(['variable', 'range']).agg(
    mean_value=('value', 'mean'),
    std_value=('value', 'std')
).reset_index()
cv_results['cv'] = cv_results['std_value'] / cv_results['mean_value']

# Pivotar la tabla para que los tipos de procesado sean columnas y los rangos filas
cv_pivot = cv_results.pivot(index='range', columns='variable', values='cv')


# Filtrar los datos para la variable 's1'
s1_data = combined_data[combined_data['variable'] == 's1']

# Contar el número de datos por rango de rendimiento para la variable 's1'
s1_count_by_range = s1_data.groupby('range').size().reset_index(name='count')

# Filtrar los datos para la variable 'G15L25'
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# Ordenar las variables según tu especificación
ordered_variables = [
    's1', 'G1', 'G15', 'G25', 'G1L1', 'G1L15', 'G1L25',
    'G15L1', 'G15L15', 'G15L25', 'G25L1', 'G25L15', 'G25L25'
]

# Filtrar los datos para el rango (0, 500) y las variables ordenadas
range_data = combined_data[combined_data['range'] == pd.Interval(0, 500)]
range_data = range_data[range_data['variable'].isin(ordered_variables)]

# Asegurarse de que las variables están en el orden especificado
range_data['variable'] = pd.Categorical(range_data['variable'], categories=ordered_variables, ordered=True)

# Crear el box and whisker plot
plt.figure(figsize=(50, 50))
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 14

range_data.boxplot(column='value', by='variable', grid=False)
plt.title('Box and Whisker Plot for Range (0, 500) by Variable', fontsize=18)
plt.suptitle('')
plt.xlabel('Variable', fontsize=16)
plt.ylabel('Value', fontsize=16)
plt.xticks(rotation=90, fontsize=14)
plt.yticks(fontsize=14)
plt.show()


import matplotlib.pyplot as plt

# Filtrar los datos para la variable s1 en el rango (0, 500)
s1_data = combined_data[(combined_data['variable'] == 's1') & (combined_data['value'] <= 500)]

# Crear el histograma
plt.figure(figsize=(10, 6), dpi=200)
plt.hist(s1_data['value'], bins=30, edgecolor='black')
plt.title('Histogram of s1 Values in Range (0, 500)', fontsize=18, fontname='Times New Roman')
plt.xlabel('Value', fontsize=16, fontname='Times New Roman')
plt.ylabel('Frequency', fontsize=16, fontname='Times New Roman')
plt.xticks(fontsize=14, fontname='Times New Roman')
plt.yticks(fontsize=14, fontname='Times New Roman')
plt.grid(axis='y', alpha=0.75)
plt.show()

