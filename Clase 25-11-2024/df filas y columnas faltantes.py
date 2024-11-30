import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo con datos faltantes
data = {
  'Nombre': ['Ana', 'Luis', 'Juan', 'María', 'Pedro'],
  'Edad': [23, pd.NA, 35, pd.NA, 28],
  'Ciudad': ['Madrid', 'Barcelona', pd.NA, 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

# Mostrar información sobre los datos faltantes
print("\nInformación sobre los datos faltantes:")
print(df.isnull().sum())

# Eliminar filas que contienen datos faltantes
df_sin_faltantes_filas = df.dropna()
print("\nDataFrame sin filas con datos faltantes:")
print(df_sin_faltantes_filas)

# Eliminar columnas que contienen datos faltantes
df_sin_faltantes_columnas = df.dropna(axis=1)
print("\nDataFrame sin columnas con datos faltantes:")
print(df_sin_faltantes_columnas)

# Opción: Eliminar filas solo si todas las columnas tienen datos faltantes
df_sin_faltantes_todas_columnas = df.dropna(how='all')
print("\nDataFrame sin filas donde todas las columnas tienen datos faltantes:")
print(df_sin_faltantes_todas_columnas)