# -*- coding: utf-8 -*-
"""
Created on Thu Jun  15 16:38:46 2024

@author: enric
"""

import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Función para calcular MAE
def calculate_mae(df, column_name):
    return df.groupby('FID')[column_name].apply(lambda x: np.mean(np.abs(x)))

"""
En los paths de los archivos shapefile se deberia de cambiar TRI por CEB para que se realice el calculo 
"""

# Leer el archivo shapefile para df_21
data_21 = "C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLsF1/TRI_21\\s1_PST.shp"
df_21 = gpd.read_file(data_21)[['FID', 'PID', 'G1L1F1']]

new_data_21 = "C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLsF1/TRI_21\\G1L15_PST.shp"
new_df_21 = gpd.read_file(new_data_21)[['FID', 'PID', 'G1L1F1']]

# Leer el archivo shapefile para df_22
data_22 = "C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLsF1/TRI_22/s1_PST.shp"
df_22 = gpd.read_file(data_22)[['FID', 'PID', 'G1L1F1']]

new_data_22 = "C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLsF1/TRI_22/G1L15_PST.shp"
new_df_22 = gpd.read_file(new_data_22)[['FID', 'PID', 'G1L1F1']]

# Asegurarse de que los DataFrames contienen las columnas necesarias
assert 'FID' in df_21.columns, "Column 'FID' is missing in the first DataFrame for df_21."
assert 'FID' in new_df_21.columns, "Column 'FID' is missing in the second DataFrame for df_21."
assert 'G1L1F1' in df_21.columns, "Column 'G1L1F1' is missing in the first DataFrame for df_21."
assert 'G1L1F1' in new_df_21.columns, "Column 'G1L1F1' is missing in the second DataFrame for df_21."

assert 'FID' in df_22.columns, "Column 'FID' is missing in the first DataFrame for df_22."
assert 'FID' in new_df_22.columns, "Column 'FID' is missing in the second DataFrame for df_22."
assert 'G1L1F1' in df_22.columns, "Column 'G1L1F1' is missing in the first DataFrame for df_22."
assert 'G1L1F1' in new_df_22.columns, "Column 'G1L1F1' is missing in the second DataFrame for df_22."

# Renombrar las columnas de G1L1F1 para evitar conflictos al fusionar
df_21 = df_21.rename(columns={'G1L1F1': 's1'})
new_df_21 = new_df_21.rename(columns={'G1L1F1': 'G1L15F1'})

df_22 = df_22.rename(columns={'G1L1F1': 's1'})
new_df_22 = new_df_22.rename(columns={'G1L1F1': 'G1L15F1'})

# Unir los DataFrames por 'FID' y 'PID' para df_21
merged_df_21 = df_21.merge(new_df_21, on=['FID','PID'])

# Eliminar la columna 'FID_y'
merged_df_21 = merged_df_21.drop(columns=['FID_y'])

# Renombrar la columna 'FID_x' a 'FID'
merged_df_21 = merged_df_21.rename(columns={'FID_x': 'FID'})

# Calcular el área basada en el número de 'PID' por 'FID' para df_21 (cada PID representa 100 metros cuadrados)
merged_df_21['area_m2'] = merged_df_21.groupby('FID')['PID'].transform('count') * 100

# Convertir el área de metros cuadrados a hectáreas para df_21
merged_df_21['area_hectareas'] = merged_df_21['area_m2'] / 10000

# Calcular el MAE para df_21 en ambos conjuntos de datos
mae_s1_21 = calculate_mae(merged_df_21, 's1')
mae_G1L15F1_21 = calculate_mae(merged_df_21, 'G1L15F1')

# Calcular la diferencia de MAE para df_21
mae_diff_21 = mae_s1_21 - mae_G1L15F1_21

# Crear el DataFrame de resultados para df_21
result_df_21 = pd.DataFrame({
    'MAE_s1': mae_s1_21,
    'MAE_G1L15F1': mae_G1L15F1_21,
    'MAE_diff': mae_diff_21,
    'area_hectareas': merged_df_21.groupby('FID')['area_hectareas'].first()  
}).reset_index()

# Unir los DataFrames por 'FID' y 'PID' para df_22
merged_df_22 = df_22.merge(new_df_22, on=['FID', 'PID'])

# Calcular el área basada en el número de 'PID' por 'FID' para df_22 (cada PID representa 100 metros cuadrados)
merged_df_22['area_m2'] = merged_df_22.groupby('FID')['PID'].transform('count') * 100

# Convertir el área de metros cuadrados a hectáreas para df_22
merged_df_22['area_hectareas'] = merged_df_22['area_m2'] / 10000

# Calcular el MAE para df_22 en ambos conjuntos de datos
mae_s1_22 = calculate_mae(merged_df_22, 's1')
mae_G1L15F1_22 = calculate_mae(merged_df_22, 'G1L15F1')

# Calcular la diferencia de MAE para df_22
mae_diff_22 = mae_s1_22 - mae_G1L15F1_22

# Crear el DataFrame de resultados para df_22
result_df_22 = pd.DataFrame({
    'MAE_s1': mae_s1_22,
    'MAE_G1L15F1': mae_G1L15F1_22,
    'MAE_diff': mae_diff_22,
    'area_hectareas': merged_df_22.groupby('FID')['area_hectareas'].first()  # Asumimos que el área es la misma para cada FID
}).reset_index()

# Combinar los resultados de ambos conjuntos
result_df_combined = pd.concat([result_df_21, result_df_22], ignore_index=True)

import pandas as pd

# Suponiendo que result_df_combined es tu DataFrame que deseas guardar

# Ruta donde quieres guardar el archivo CSV
ruta_guardado = "C:/Users/enric/Escritorio/UPV\\,TFM\\VALIDACION\\postprocesing_TRI"

# Guardar el DataFrame como archivo CSV
result_df_combined.to_csv(ruta_guardado, index=False)

print(f"Archivo guardado exitosamente en: {ruta_guardado}")

"""
Graficado de los resultados conjuntos 
"""

import pandas as pd
import matplotlib.pyplot as plt

# Definir las rutas de los archivos
ruta_postpro_TRI = "C:/Users/enric/Escritorio/UPV\\,TFM\\VALIDACION\\postprocesing_CEB"

ruta_postpro_CEB = "C:/Users/enric/Escritorio/UPV\\,TFM\\VALIDACION\\postprocesing_TRI"

# Leer los archivos CSV en DataFrames
df_postpro_TRI = pd.read_csv(ruta_postpro_TRI)
df_postpro_CEB = pd.read_csv(ruta_postpro_CEB)

total_TRI = len(df_postpro_TRI)
total_CEB = len(df_postpro_CEB)

"""
Calcular los porcentajes de camposentre 0 y ±100 kg/ha, ±100 kg/ha y ±200 kg/ha y fuera de ±200 kg/ha  para df_postpro_CEB
"""

fuera_rango_CEB = len(df_postpro_CEB[(df_postpro_CEB['MAE_diff'] > 200) | (df_postpro_CEB['MAE_diff'] < -200)])
porcentaje_fuera_rango_CEB = (fuera_rango_CEB / total_CEB) * 100
entre_rango_CEB = len(df_postpro_CEB[(df_postpro_CEB['MAE_diff'] >= 0) & (df_postpro_CEB['MAE_diff'] <= 100) | (df_postpro_CEB['MAE_diff'] <= 0) & (df_postpro_CEB['MAE_diff'] >= -100)])
porcentaje_entre_rango_CEB = (entre_rango_CEB / total_CEB) * 100
entre_rango_CEB = len(df_postpro_CEB[((df_postpro_CEB['MAE_diff'] > 100) & (df_postpro_CEB['MAE_diff'] <= 200)) | ((df_postpro_CEB['MAE_diff'] < -100) & (df_postpro_CEB['MAE_diff'] >= -200))])
porcentaje_entre_rango_CEB = (entre_rango_CEB / total_CEB) * 100

# Imprimir los resultados
print(f"Porcentaje de campos entre 0 y ±100 kg/ha en df_postpro_CEB: {porcentaje_entre_rango_CEB:.2f}%")
print(f"Porcentaje de campos entre ±100 kg/ha y ±200 kg/ha en df_postpro_CEB: {porcentaje_entre_rango_CEB:.2f}%")
print(f"Porcentaje de campos fuera del rango ±200 kg/ha en df_postpro_CEB: {porcentaje_fuera_rango_CEB:.2f}%")

"""
Calcular los porcentajes de camposentre 0 y ±100 kg/ha, ±100 kg/ha y ±200 kg/ha y fuera de ±200 kg/ha  para df_postpro_TRI
"""

entre_rango_TRI = len(df_postpro_TRI[(df_postpro_TRI['MAE_diff'] >= 0) & (df_postpro_TRI['MAE_diff'] <= 100) | (df_postpro_TRI['MAE_diff'] <= 0) & (df_postpro_TRI['MAE_diff'] >= -100)])
porcentaje_entre_rango_TRI = (entre_rango_TRI / total_TRI) * 100
entre_rango_TRI = len(df_postpro_TRI[((df_postpro_TRI['MAE_diff'] > 100) & (df_postpro_TRI['MAE_diff'] <= 200)) | ((df_postpro_TRI['MAE_diff'] < -100) & (df_postpro_TRI['MAE_diff'] >= -200))])
porcentaje_entre_rango_TRI = (entre_rango_TRI / total_TRI) * 100
fuera_rango_TRI = len(df_postpro_TRI[(df_postpro_TRI['MAE_diff'] > 200) | (df_postpro_TRI['MAE_diff'] < -200)])
porcentaje_fuera_rango_TRI = (fuera_rango_TRI / total_TRI) * 100

# Imprimir los resultados

print(f"Porcentaje de campos entre 0 y ±100 kg/ha en df_postpro_TRI: {porcentaje_entre_rango_TRI:.2f}%")
print(f"Porcentaje de campos entre ±100 kg/ha y ±200 kg/ha en df_postpro_TRI: {porcentaje_entre_rango_TRI:.2f}%")
print(f"Porcentaje de campos fuera del rango ±200 kg/ha en df_postpro_TRI: {porcentaje_fuera_rango_TRI:.2f}%")


"""
Calcular los porcentajes de campos por debajo de 1 ha, entre 1 ha y 2.5 ha y por encima de 2.5 ha para df_postpro_TRI
"""

total_TRI = len(df_postpro_TRI)
menos_1ha_TRI = len(df_postpro_TRI[df_postpro_TRI['area_hectareas'] < 1])
entre_1ha_25ha_TRI = len(df_postpro_TRI[(df_postpro_TRI['area_hectareas'] >= 1) & (df_postpro_TRI['area_hectareas'] <= 2.5)])
porcentaje_menos_1ha_TRI = (menos_1ha_TRI / total_TRI) * 100
porcentaje_entre_1ha_25ha_TRI = (entre_1ha_25ha_TRI / total_TRI) * 100
por_encima_25ha_TRI = len(df_postpro_TRI[df_postpro_TRI['area_hectareas'] > 2.5])
porcentaje_por_encima_25ha_TRI = (por_encima_25ha_TRI / total_TRI) * 100

# Imprimir los resultados

print(f"Porcentaje de campos por debajo de 1 ha en df_postpro_TRI: {porcentaje_menos_1ha_TRI:.2f}%")
print(f"Porcentaje de campos entre 1 ha y 2.5 ha en df_postpro_TRI: {porcentaje_entre_1ha_25ha_TRI:.2f}%")
print(f"Porcentaje de campos por encima de 2.5 ha en df_postpro_TRI: {porcentaje_por_encima_25ha_TRI:.2f}%")

"""
Calcular los porcentajes de campos por debajo de 1 ha, entre 1 ha y 2.5 ha y por encima de 2.5 ha para df_postpro_CEB
"""


menos_1ha_CEB = len(df_postpro_CEB[df_postpro_CEB['area_hectareas'] < 1])
entre_1ha_25ha_CEB = len(df_postpro_CEB[(df_postpro_CEB['area_hectareas'] >= 1) & (df_postpro_CEB['area_hectareas'] <= 2.5)])
porcentaje_menos_1ha_CEB = (menos_1ha_CEB / total_CEB) * 100
porcentaje_entre_1ha_25ha_CEB = (entre_1ha_25ha_CEB / total_CEB) * 100
por_encima_25ha_CEB = len(df_postpro_CEB[df_postpro_CEB['area_hectareas'] > 2.5])
porcentaje_por_encima_25ha_CEB = (por_encima_25ha_CEB / total_CEB) * 100

# Imprimir los resultados

print(f"Porcentaje de campos por debajo de 1 ha en df_postpro_CEB: {porcentaje_menos_1ha_CEB:.2f}%")
print(f"Porcentaje de campos entre 1 ha y 2.5 ha en df_postpro_CEB: {porcentaje_entre_1ha_25ha_CEB:.2f}%")
print(f"Porcentaje de campos por encima de 2.5 ha en df_postpro_CEB: {porcentaje_por_encima_25ha_CEB:.2f}%")

# Crear el gráfico de dispersión
plt.figure(figsize=(20, 20))  # Ajustar el tamaño según sea necesario

# Graficar los datos del primer DataFrame
plt.scatter(df_postpro_TRI['area_hectareas'], df_postpro_TRI['MAE_diff'], s=200, alpha=0.75, color='blue', label='Trigo', marker='o')

# Graficar los datos del segundo DataFrame
plt.scatter(df_postpro_CEB['area_hectareas'], df_postpro_CEB['MAE_diff'], s=200, alpha=0.75, color='red', label='Cebada', marker='^')

# Configurar etiquetas y título
plt.xlabel('Área (ha)', fontsize=30)
plt.ylabel('Diferencia en kg/ha', fontsize=30)
plt.grid(True)
plt.legend(fontsize=30)
# Añadir una línea horizontal en y=0
plt.axhline(y=0, color='black', linestyle='--', linewidth=5)

# Mostrar el gráfico
plt.show()
