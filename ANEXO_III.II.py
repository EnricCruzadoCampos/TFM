# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:38:48 2024

@author: enric
"""

import os
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

"""
Cambiar en la ruta del archivo shape file TRI por CEB para graficar el histograma del cultivo deseado
"""

# Rutas a los archivos Shapefile para df_21 y df_22
shapefile_path_21 = "C:/Users/enric/Escritorio/UPV/,TFM/QGIS/Tri21/10x10_TRI_21.shp"
shapefile_path_22 = "C:/Users/enric/Escritorio/UPV/,TFM/QGIS/Tri22/10x10_TRI_22.shp"

# Lista de nombres de las variables de interés en los archivos
variables = ['s1_range', 'G1_range', 'G15_range', 'G25_range', 
             'G1L1_range', 'G1L15_rang', 'G1L25_rang', 
             'G15L1_rang', 'G15L15_ran', 'G15L25_ran',
             'G25L1_rang', 'G25L15_ran', 'G25L25_ran']

# Tamaño base para la figura y otros elementos
base_size = 30

# Factor de escala para ajustar el tamaño
scale_factor = 5.5

# Graficar histogramas de frecuencias acumuladas en el mismo gráfico
fig, ax = plt.subplots(figsize=(base_size * scale_factor, base_size * scale_factor))

# Cargar los archivos Shapefile
gdf_21 = gpd.read_file(shapefile_path_21)
gdf_22 = gpd.read_file(shapefile_path_22)

# Concatenar los GeoDataFrames
gdf = gpd.GeoDataFrame(pd.concat([gdf_21, gdf_22], ignore_index=True))

for var in variables:
    # Eliminar valores nulos
    gdf_var = gdf.dropna(subset=[var])
    
    # Depuración: imprimir el nombre de variable procesada
    print(f"Procesando variable: {var}")

    # Extraer las variables de interés
    values = gdf_var[var].values

    # Calcular el porcentaje de valores
    total_values = len(values)
    hist, bins = np.histogram(values, bins=20)
    percentages = (np.cumsum(hist) / total_values) * 100

    # Definir el estilo de línea: discontinua para 's1_range', continua para el resto
    linestyle = '--' if var == 's1_range' else '-'
    
    # Extraer la parte anterior al carácter '_'
    legend_label = var.split('_')[0]
    
    # Graficar el histograma de frecuencias acumuladas con líneas
    ax.plot(bins[:-1], percentages, label=legend_label, linestyle=linestyle, linewidth=10 * scale_factor)

# Ajustar los límites del eje x
ax.set_xlim([0, 5000])  # Establece el rango adecuado para tus datos

# Ajustar los títulos y etiquetas con la fuente Times New Roman y más espacio
ax.set_xlabel('Rango (kg/ha)', fontsize=60 * scale_factor, labelpad=30, fontname='Times New Roman')
ax.set_ylabel('Pixeles (%)', fontsize=60 * scale_factor, labelpad=30, fontname='Times New Roman')
ax.set_title('Histograma Trigo', fontsize=80 * scale_factor, pad=50, fontname='Times New Roman')
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
