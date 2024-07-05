# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:41:33 2024

@author: enric
"""
import geopandas as gpd
import pandas as pd
from scipy.stats import f_oneway
import os

"""
En los paths de los archivos shapefile se deberia de cambiar TRI por CEB para que se realice el calculo 
"""

# Lista de rutas a los archivos shapefiles para el año 2021 y 2022

shapefile_paths_21 = [
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_21\\SHAPE\\s1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_21\\SHAPE\\G1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_21\\SHAPE\\G15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_21\\SHAPE\\G25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G1LsA\\G1L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G1LsA\\G1L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G1LsA\\G1L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G15Ls\\G15L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G15Ls\\G15L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G15Ls\\G15L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G25Ls\\G25L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G25Ls\\G25L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_21\\G25Ls\\G25L25_SAMPLED.shp",
]

shapefile_paths_22 = [
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_22\\SHAPE\\s1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_22\\SHAPE\\G1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_22\\SHAPE\\G15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsAA\\BUR_CEB_22\\SHAPE\\G25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G1LsA\\G1L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G1LsA\\G1L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G1LsA\\G1L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G15Ls\\G15L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G15Ls\\G15L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G15Ls\\G15L25_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G25Ls\\G25L1_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G25Ls\\G25L15_SAMPLED.shp",
    "C:/Users/enric/Escritorio/UPV\\,TFM\\CV_GsLs\\BUR_CEB_22\\G25Ls\\G25L25_SAMPLED.shp",
]

# Lista de nombres de las variables de interés
variables = [    's1_1', 'G1_1', 'G15_1', 'G25_1', 'G1L1_1', 'G1L15_1', 'rvalue_1', 
    'G1L1_1', 'G1L15_1', 'rvalue_1', 'G1L1_1', 'G1L15_1', 'rvalue_1']

# Combina las dos listas de shapefiles
shapefile_paths = shapefile_paths_21 + shapefile_paths_22

# Diccionario para almacenar los resultados
results = {}

# Leer cada archivo shapefile y extraer los datos relevantes
for filepath, variable in zip(shapefile_paths, variables):
    gdf = gpd.read_file(filepath)
    
    # Verificar si la columna de interés está en el GeoDataFrame
    if variable in gdf.columns:
        values = gdf[variable].dropna().tolist()
        
        # Calcular la media y la desviación estándar
        mean_value = pd.Series(values).mean()
        std_deviation = pd.Series(values).std()
        
        # Guardar los resultados en el diccionario
        filename = os.path.basename(filepath)
        results[(filename, variable)] = (mean_value, std_deviation)

# Mostrar los resultados
for (filename, variable), stats in results.items():
    mean_value, std_deviation = stats
    print(f"Archivo: {filename}")
    print(f"Variable: {variable}")
    print(f"Media: {mean_value}")
    print(f"Desviación estándar: {std_deviation}")
    print()
