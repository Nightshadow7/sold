import pandas as pd

# Crear un DataFrame de ejemplo con datos faltantes
data = {
  'Nombre': ['Ana', 'Luis', 'Juan', 'María', 'Pedro'],
  'Edad': [23, pd.NA, 35, pd.NA, 28],
  'Ciudad': ['Madrid', 'Barcelona', pd.NA, 'Valencia', 'Sevilla']
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