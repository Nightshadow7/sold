import pandas as pd

# Crear un DataFrame de ejemplo con datos duplicados
data = {
  'Nombre': ['Ana', 'Luis', 'Juan', 'Ana', 'Pedro', 'Luis'],
  'Edad': [23, 30, 35, 23, 28, 30],
  'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Sevilla', 'Barcelona']
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

# Identificar datos duplicados
duplicados = df.duplicated()
print("\nDatos duplicados (True significa que la fila es duplicada):")
print(duplicados)

# Contar el número de filas duplicadas
num_duplicados = df.duplicated().sum()
print(f"\nNúmero de filas duplicadas: {num_duplicados}")

# Eliminar filas duplicadas
df_sin_duplicados = df.drop_duplicates()
print("\nDataFrame sin filas duplicadas:")
print(df_sin_duplicados)

# Eliminar duplicados considerando solo ciertas columnas
df_sin_duplicados_columnas = df.drop_duplicates(subset=['Nombre', 'Ciudad'])
print("\nDataFrame sin duplicados considerando solo 'Nombre' y 'Ciudad':")
print(df_sin_duplicados_columnas)

# Conservar solo la última ocurrencia de duplicados
df_ultima_ocurrencia = df.drop_duplicates(keep='last')
print("\nDataFrame conservando solo la última ocurrencia de duplicados:")
print(df_ultima_ocurrencia)