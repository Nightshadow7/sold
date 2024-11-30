import numpy as np
import pandas as pd

data = {
  'Nombre': ['Ana', 'Luis', 'Juan', 'María', 'Pedro'],
  'Edad': [23, np.nan, 35, np.nan, 28],
  'Ciudad': ['Madrid', 'Barcelona', np.nan, 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

# Identificar valores faltantes
print("\nValores faltantes:")
print(df.isnull().sum())

# Eliminar filas con valores faltantes
df_sin_faltantes = df.dropna()
print("\nDataFrame sin filas con datos faltantes:")
print(df_sin_faltantes)

# Rellenar valores faltantes con un valor específico
df_rellenado = df.fillna({'Edad': df['Edad'].mean(), 'Ciudad': 'Desconocida'})
print("\nDataFrame con valores faltantes rellenados:")
print(df_rellenado)