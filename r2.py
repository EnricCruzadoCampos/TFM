# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:33:13 2024

@author: enric
"""

import numpy as np
import geopandas as gpd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

"""
Cambiar en archivo_con_rendimientos_y_bandas el nivel de postprocesado deseado y CEB por TRI para calcular la r2 en trigo
"""
data = "C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs\\CEB_21\\archivo_con_rendimientos_y_bandas.shp"

df = gpd.read_file(data)
df_point = df.drop("geometry", axis=1)
df_clean = df_point.dropna(subset=["G1L1F1"])


#SCRIP INICIAL
fechas_unicas = df_clean.columns.str.split('_').str[0].unique()

# Listas para almacenar los resultados de R^2 para cada fecha
resultados_r2 = []

# Iterar sobre cada fecha única
for fecha in fechas_unicas:
    # Seleccionar las columnas correspondientes a la fecha actual
    columnas_fecha = [col for col in df_clean.columns if col.startswith(fecha)]

    # Definir las variables independientes (bandas) y dependiente (rendimiento)
    X = df_clean[columnas_fecha].values
    y = df_clean['G1L1F1'].values

    # Ajustar el modelo de regresión lineal múltiple
    model = LinearRegression()
    model.fit(X, y)

    # Predecir los valores
    y_pred = model.predict(X)

    # Calcular R^2
    r2 = r2_score(y, y_pred)

    # Almacenar el resultado de R^2 para la fecha actual
    resultados_r2.append((fecha, r2))

# Imprimir los resultados
for fecha, r2 in resultados_r2:
    print(f"Fecha: {fecha}, Coeficiente de Determinación (R^2): {r2}")
    
resultados_r2_2 = resultados_r2[3:20]

# Convertir los resultados en un DataFrame para facilitar la manipulación
resultados_df = pd.DataFrame(resultados_r2_2, columns=['Fecha', 'R^2'])

# Ordenar los resultados por fecha
resultados_df = resultados_df.sort_values(by='Fecha')


# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(resultados_df['Fecha'], resultados_df['R^2'], marker='o', linestyle='-')
plt.xlabel('Fecha')
plt.ylabel('Coeficiente de Determinación (R^2)')
plt.title('Coeficiente de Determinación (R^2) en función de la fecha')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
