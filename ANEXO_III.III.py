# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:48:30 2024

@author: enric
"""

import os
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging
from skgstat import Variogram

"""
En los paths de los archivos shapefile se deberia de cambiar TRI por CEB para que se realice el calculo 
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
variables = ['s1_1', 'G1_1', 'G15_1', 'G25_1', 'G1L1_1', 'G1L15_1', 'rvalue_1', 
             'G1L1_1', 'G1L15_1', 'rvalue_1', 'G1L1_1', 'G1L15_1', 'rvalue_1']

# Configurar parámetros de variograma
n_lags = 50
maxlag = 400

# Tamaño base para la figura y otros elementos
base_size = 30

# Factor de escala para ajustar el tamaño
scale_factor = 5.5

# Graficar varios semivariogramas en el mismo gráfico
fig, ax = plt.subplots(figsize=(base_size * scale_factor, base_size * scale_factor))

# Definir la distancia a eliminar
distance_to_remove = 8

for shapefile_path_22, var in zip(shapefile_paths_22, variables):
    # Crear la ruta correspondiente para BUR_CEB_21
    shapefile_path_21 = shapefile_path_22.replace("BUR_CEB_22", "BUR_CEB_21")
    
    # Cargar los archivos Shapefile
    gdf_22 = gpd.read_file(shapefile_path_22)
    gdf_21 = gpd.read_file(shapefile_path_21)
    
    # Concatenar los GeoDataFrames
    gdf = gpd.GeoDataFrame(pd.concat([gdf_22, gdf_21], ignore_index=True))
    
    # Eliminar valores nulos
    gdf = gdf.dropna(subset=[var])
    
    # Extraer el nombre del archivo desde el último slash '/' o backslash '\' hasta '_'
    start_index = max(shapefile_path_22.rfind('/'), shapefile_path_22.rfind('\\')) + 1
    end_index = shapefile_path_22.find('_', start_index)
    filename = shapefile_path_22[start_index:end_index]
    
    # Depuración: imprimir el nombre de archivo extraído
    print(f"Extrayendo filename: {filename} de {shapefile_path_22} y {shapefile_path_21}")

    # Extraer las coordenadas y las variables de interés
    coords = np.array([(geom.x, geom.y) for geom in gdf.geometry])
    values = gdf[var].values
    
    # Calcular el variograma experimental
    variogram = Variogram(coords, values, model='exponential', n_lags=n_lags, maxlag=maxlag)
    distances = variogram.bins
    semivariances = variogram.experimental
    
    # Filtrar la distancia específica
    mask = distances != distance_to_remove
    distances = distances[mask]
    semivariances = semivariances[mask]
    
    # Graficar el variograma experimental, ajustando las semivarianzas
    ax.plot(distances, semivariances / 1000000, marker='o', label=filename, markersize=25 * scale_factor, linewidth=10 * scale_factor)

# Ajustar los títulos y etiquetas
ax.set_xlabel('Distancia (m)', fontsize=60 * scale_factor, labelpad=20, fontname='Times New Roman')
ax.set_ylabel('Semivarianza (millones)', fontsize=60 * scale_factor, labelpad=20, fontname='Times New Roman')
ax.set_title('Comparación de los Semivariogramas', fontsize=80 * scale_factor, pad=30, fontname='Times New Roman')
ax.grid(True, linewidth=5 * scale_factor)
ax.tick_params(axis='both', which='major', labelsize=50 * scale_factor, pad=15, direction='inout')
ax.tick_params(axis='both', which='minor', labelsize=50 * scale_factor, pad=15, direction='inout')
legend = ax.legend(fontsize=50 * scale_factor, bbox_to_anchor=(1.05, 1), loc='upper left')
for text in legend.get_texts():
    text.set_fontname("Times New Roman")

# Cambiar la fuente de los números de los ejes a Times New Roman
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname('Times New Roman')

plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1)
ax.spines['bottom'].set_linewidth(5 * scale_factor)
ax.spines['left'].set_linewidth(5 * scale_factor)

plt.show()
