# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:35:22 2024

@author: enric
"""

"""
Cálculo de porcentaje de Polígonos, Píxeles eliminados y Coeficiente de Variación para los postrpocesados con ajuste global
"""

import geopandas as gpd

#Carga de DATOS SAMPLED
S1_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/s1_SAMPLED.shp'
G1_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G1_SAMPLED.shp'
G15_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G15_SAMPLED.shp'
G2_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G2_SAMPLED.shp'
G25_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G25_SAMPLED.shp'
G3_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G3_SAMPLED.shp'

#Lectura de los DATOS SAMPLED
S1 = gpd.read_file(S1_SAMPLED)
G1 = gpd.read_file(G1_SAMPLED)
G15 = gpd.read_file(G15_SAMPLED)
G2 = gpd.read_file(G2_SAMPLED)
G25 = gpd.read_file(G25_SAMPLED)
G3 = gpd.read_file(G3_SAMPLED)

#Carga de POLIGONOS DE LA COSECHADORA
S1_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/s1_shp.shp'
G1_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G1_shp.shp'
G15_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G15_shp.shp'
G2_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G2_shp.shp'
G25_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G25_shp.shp'
G3_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/G3_shp.shp'

#Lectura de POLIGONOS DE LA COSECHADORA
S1_POLI = gpd.read_file(S1_SHP)
G1_POLI = gpd.read_file(G1_SHP)
G15_POLI = gpd.read_file(G15_SHP)
G2_POLI = gpd.read_file(G2_SHP)
G25_POLI = gpd.read_file(G25_SHP)
G3_POLI = gpd.read_file(G3_SHP)

#S1
#Numero de pixeles eliminados
null_count_S1_= S1['s1_1'].isnull().sum()

print(f"Pixeles eliminados en S1: {null_count_S1_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsS1 = len(S1)
porcentaje_eliminadosS1 = (null_count_S1_ / total_rowsS1) * 100

print(f"Porcentaje de Pixeles eliminados en S1 {porcentaje_eliminadosS1:.2f}%")

# Eliminar filas con valores nulos en la columna S1_1
S1_cleaned = S1.dropna(subset=['s1_1'])

#Calculo CV 
mS1 = S1_cleaned['s1_1'].mean()
stdS1 = S1_cleaned['s1_1'].std()
cvS1 = (stdS1 / mS1) * 100

print("La media es:",  mS1,"kg_ha")
print("La desviación estandar es:",  stdS1,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvS1:.2f}%")


#G1
#Numero de pixeles eliminados
null_count_G1_= G1['G1_1'].isnull().sum()

print(f"Pixeles eliminados en G1: {null_count_G1_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsG1 = len(G1)
porcentaje_eliminadosG1 = (null_count_G1_ / total_rowsG1) * 100

print(f"Porcentaje de Pixeles eliminados en G1 {porcentaje_eliminadosG1:.2f}%")

#Calculo de POLIGONOS ELIMINADOS
total__poli = len(S1_POLI)
percent_eli_poliG1 = 100 - ( len(G1_POLI)/ total__poli) * 100

print(f"Porcentaje de Poligonos eliminados en G1 {percent_eli_poliG1:.2f}%")

# Eliminar filas con valores nulos en la columna G1_1
G1_cleaned = G1.dropna(subset=['G1_1'])

#Calculo CV 
mG1 = G1_cleaned['G1_1'].mean()
stdG1 = G1_cleaned['G1_1'].std()
cvG1 = (stdG1 / mG1) * 100

print("La media es:",  mG1,"kg_ha")
print("La desviación estandar es:",  stdG1,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvG1:.2f}%")

#G15
#Numero de pixeles eliminados
null_count_G15_= G15['G15_1'].isnull().sum()

print(f"Pixeles eliminados en G15: {null_count_G15_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsG15 = len(G15)
porcentaje_eliminadosG15 = (null_count_G15_ / total_rowsG15) * 100

print(f"Porcentaje de Pixeles eliminados en G15 {porcentaje_eliminadosG15:.2f}%")

#Calculo de POLIGONOS ELIMINADOS
percent_eli_poliG15 = 100 -(len(G15_POLI) / total__poli) * 100

print(f"Porcentaje de Poligonos eliminados en G15 {percent_eli_poliG15:.2f}%")

# Eliminar filas con valores nulos en la columna G15_1
G15_cleaned = G15.dropna(subset=['G15_1'])

#Calculo CV 
mG15 = G15_cleaned['G15_1'].mean()
stdG15 = G15_cleaned['G15_1'].std()
cvG15 = (stdG15 / mG15) * 100

print("La media es:",  mG15,"kg_ha")
print("La desviación estandar es:",  stdG15,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvG15:.2f}%")

#G25
#Numero de pixeles eliminados
null_count_G25_= G25['G25_1'].isnull().sum()

print(f"Pixeles eliminados en G25: {null_count_G25_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsG25 = len(G25)
porcentaje_eliminadosG25 = (null_count_G25_ / total_rowsG25) * 100

print(f"Porcentaje de Pixeles eliminados en G25 {porcentaje_eliminadosG25:.2f}%")

#Calculo de POLIGONOS ELIMINADOS
percent_eli_poliG25 = 100 -(len(G25_POLI) / total__poli) * 100

print(f"Porcentaje de Poligonos eliminados en G25 {percent_eli_poliG25:.2f}%")

# Eliminar filas con valores nulos en la columna G25_1
G25_cleaned = G25.dropna(subset=['G25_1'])

#Calculo CV 
mG25 = G25_cleaned['G25_1'].mean()
stdG25 = G25_cleaned['G25_1'].std()
cvG25 = (stdG25 / mG25) * 100

print("La media es:",  mG25,"kg_ha")
print("La desviación estandar es:",  stdG25,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvG25:.2f}%")

"""
Cálculo de porcentaje de Polígonos, Píxeles eliminados y Coeficiente de Variación para los postrpocesados con ajuste global + local
"""

import geopandas as gpd

#Carga de DATOS SAMPLED
GsL1_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs/BUR_CEB_21/G25Ls/GsL1_SAMPLED.shp'
GsL15_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs/BUR_CEB_21/G25Ls/GsL15_SAMPLED.shp'
GsL25_SAMPLED = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs/BUR_CEB_21/G25Ls/GsL25_SAMPLED.shp'

#Lectura de los DATOS SAMPLED
GsL1 = gpd.read_file(GsL1_SAMPLED)
GsL15 = gpd.read_file(GsL15_SAMPLED)
GsL25 = gpd.read_file(GsL25_SAMPLED)

#Carga de POLIGONOS DE LA COSECHADORA
Gs_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_Gs/BUR_CEB_21/SHAPES/s1_shp.shp'
GsL1_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs/BUR_CEB_21/G25Ls/GsL1_shp.shp'
GsL15_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs/BUR_CEB_21/G25Ls/GsL15_shp.shp'
GsL25_SHP = 'C:/Users/enric/Escritorio/UPV/,TFM/CV_GsLs/BUR_CEB_21/G25Ls/GsL25_shp.shp'

#Lectura de POLIGONOS DE LA COSECHADORA
Gs_POLI = gpd.read_file(Gs_SHP)
GsL1_POLI = gpd.read_file(GsL1_SHP)
GsL15_POLI = gpd.read_file(GsL15_SHP)
GsL25_POLI = gpd.read_file(GsL25_SHP)


#GsL1
#GsL1_f = GsL1[GsL1['FID'] != 39]
GsL1_filtered = GsL1[GsL1['FID'] != 11]

#Numero de pixeles eliminados
null_count_GsL1_= GsL1_filtered['G1L1_1'].isnull().sum()

print(f"Pixeles eliminados en GsL1: {null_count_GsL1_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsGsL1 = len(GsL1_filtered)
porcentaje_eliminadosGsL1 = (null_count_GsL1_ / total_rowsGsL1) * 100

print(f"Porcentaje de Pixeles eliminados en GsL1 {porcentaje_eliminadosGsL1:.2f}%")

#Calculo de POLIGONOS ELIMINADOS
total__poli = len(Gs_POLI)
percent_eli_poliGsL1 = 100 - ( len(GsL1_POLI)/ total__poli) * 100

print(f"Porcentaje de Poligonos eliminados en GsL1 {percent_eli_poliGsL1:.2f}%")

# Eliminar filas con valores nulos en la columna G1_1
GsL1_cleaned = GsL1.dropna(subset=['G1L1_1'])

#Calculo CV 
mGsL1 = GsL1_cleaned['G1L1_1'].mean()
stdGsL1 = GsL1_cleaned['G1L1_1'].std()
cvGsL1 = (stdGsL1 / mGsL1) * 100

print("La media es:",  mGsL1,"kg_ha")
print("La desviación estandar es:",  stdGsL1,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvGsL1:.2f}%")

#GsL15
GsL15_filtered = GsL15[GsL1['FID'] != 11]
#Numero de pixeles eliminados
null_count_GsL15_= GsL15_filtered['G1L15_1'].isnull().sum()

print(f"Pixeles eliminados en GsL15: {null_count_GsL15_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsGsL15 = len(GsL15_filtered)
porcentaje_eliminadosGsL15 = (null_count_GsL15_ / total_rowsGsL15) * 100

print(f"Porcentaje de Pixeles eliminados en GsL15 {porcentaje_eliminadosGsL15:.2f}%")

#Calculo de POLIGONOS ELIMINADOS
percent_eli_poliGsL15 = 100 -(len(GsL15_POLI) / total__poli) * 100

print(f"Porcentaje de Poligonos eliminados en G15 {percent_eli_poliGsL15:.2f}%")

# Eliminar filas con valores nulos en la columna G15_1
GsL15_cleaned = GsL15.dropna(subset=['G1L15_1'])

#Calculo CV 
mGsL15 = GsL15_cleaned['G1L15_1'].mean()
stdGsL15 = GsL15_cleaned['G1L15_1'].std()
cvGsL15 = (stdGsL15 / mGsL15) * 100

print("La media es:",  mGsL15,"kg_ha")
print("La desviación estandar es:",  stdGsL15,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvGsL15:.2f}%")

#GsL25
GsL25_filtered = GsL25[GsL1['FID'] != 11]
#Numero de pixeles eliminados
null_count_GsL25_= GsL25_filtered['rvalue_1'].isnull().sum()

print(f"Pixeles eliminados en GsL25: {null_count_GsL25_}")

# Calcular el porcentaje de valores nulos eliminados
total_rowsGsL25 = len(GsL25_filtered)
porcentaje_eliminadosGsL25 = (null_count_GsL25_ / total_rowsGsL25) * 100

print(f"Porcentaje de Pixeles eliminados en GsL25 {porcentaje_eliminadosGsL25:.2f}%")

#Calculo de POLIGONOS ELIMINADOS
percent_eli_poliGsL25 = 100 -(len(GsL25_POLI) / total__poli) * 100

print(f"Porcentaje de Poligonos eliminados en G25 {percent_eli_poliGsL25:.2f}%")

# Eliminar filas con valores nulos en la columna G25_1
GsL25_cleaned = GsL25.dropna(subset=['rvalue_1'])

#Calculo CV 
mGsL25 = GsL25_cleaned['rvalue_1'].mean()
stdGsL25 = GsL25_cleaned['rvalue_1'].std()
cvGsL25 = (stdGsL25 / mGsL25) * 100

print("La media es:",  mGsL25,"kg_ha")
print("La desviación estandar es:",  stdGsL25,"kg_ha")
print(f"El Coeficiente de Variación es:  {cvGsL25:.2f}%")


from tabulate import tabulate

#PIXELES EN %
percentGsL1 =f"{porcentaje_eliminadosGsL1:.2f}".replace('.', ',') + "%"
percentGsL15 =f"{porcentaje_eliminadosGsL15:.2f}".replace('.', ',') + "%"
percentGsL25 = f"{porcentaje_eliminadosGsL25:.2f}".replace('.', ',') + "%"

#POLIGONOS EN %
percentPOLIGsL1 = f"{percent_eli_poliGsL1:.2f}".replace('.', ',') + "%"
percentPOLIGsL15 = f"{percent_eli_poliGsL15:.2f}".replace('.', ',') + "%"
percentPOLIGsL25 = f"{percent_eli_poliGsL25:.2f}".replace('.', ',') + "%"

#CV EN%
percentcvGsL1=f"{cvGsL1:.2f}".replace('.', ',') + "%"
percentcvGsL15=f"{cvGsL15:.2f}".replace('.', ',') + "%"
percentcvGsL25=f"{cvGsL25:.2f}".replace('.', ',') + "%"

# Definir variables
GsLs = ["L1","L15","L25"]
PIXELES = [percentGsL1, percentGsL15, percentGsL25 ]
POLIGONOS = [percentPOLIGsL1, percentPOLIGsL15 , percentPOLIGsL25]
CV = [percentcvGsL1,percentcvGsL15  ,percentcvGsL25 ]

# Combinar las variables en una lista de listas
data = list(zip(GsLs,PIXELES, POLIGONOS, CV))

# Encabezados de la tabla
headers = ["GsLs",'PIXELES', 'POLIGONOS', 'CV']

# Mostrar la tabla
print(tabulate(data, headers))
