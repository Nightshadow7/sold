import numpy as np
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# 1. Cargar los datos desde un archivo Excel
df = pd.read_excel(r'C:\Users\herna\Music\Ciencia de datos\clase 26-11-2024\terceros.xlsx', sheet_name='terceros')


# • Visualizar datos faltantes
msno.matrix(df)
plt.show()
# También puedes usar el gráfico de barras
msno.bar(df)
plt.show()

# •	Eliminar filas con valores faltantes
# Identificar valores faltantes
print("\nValores faltantes:")
print(df.isnull().sum())
# 5.2. Calcular el porcentaje de valores faltantes
faltantes_porcentaje = df.isnull().mean() * 100
print("\nPorcentaje de valores faltantes por columna:")
print(faltantes_porcentaje)

# Eliminar filas con valores faltantes
df_sin_faltantes = df.dropna()
print("\nDataFrame sin filas con datos faltantes:")
print(df_sin_faltantes)
msno.matrix(df_sin_faltantes)
plt.show()

# •	Rellenar valores faltantes con un valor específico
# Rellenar valores faltantes con un valor específico
df_rellenado = df.fillna({'Edad': df['Edad'].mean(), 'Telefono': +5700000000, 'Ciudad': 'Desconocida', 'Ocupacion': 'Zangano' , 'Comentarios': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita soluta similique dignissimos deserunt sapiente nulla perferendis, iusto aperiam corrupti aut cum nemo quisquam. Nostrum voluptates voluptatem non. Ab, similique eaque.'})
print("\nDataFrame con valores faltantes rellenados:")
print(df_rellenado)
msno.matrix(df_rellenado)
plt.show()

# 5.3. Crear un DataFrame para visualizar los valores faltantes en detalle
datos_faltantes = pd.DataFrame({
  'Columna': df.columns,
  'Valores_Faltantes': df.isnull().sum(),
  'Porcentaje': faltantes_porcentaje
})
print("\nTabla de valores faltantes:")
print(datos_faltantes)

# 5.4. Opcional: Gráfico de barras con Matplotlib para valores faltantes
faltantes_porcentaje.plot(kind='bar', figsize=(10, 6), color='orange')
plt.title('Porcentaje de valores faltantes por columna')
plt.xlabel('Columnas')
plt.ylabel('Porcentaje')
plt.show()

# 6.1. Visualizar matriz de valores faltantes
msno.matrix(df)
plt.title('Matriz de valores faltantes')
plt.show()

# 6.2. Visualizar un gráfico de barras para la cantidad de datos faltantes por columna
msno.bar(df)
plt.title('Cantidad de valores faltantes por columna')
plt.show()

# 6.3. (Opcional) Visualizar correlación de valores faltantes entre columnas
msno.heatmap(df)
plt.title('Correlación de valores faltantes')
plt.show()

# Mostrar la cantidad de valores faltantes por columna
print("\nCantidad de valores faltantes por columna:")
print(df.isnull().sum())

# Mostrar el porcentaje de valores faltantes por columna
faltantes_porcentaje = df.isnull().mean() * 100
print("\nPorcentaje de valores faltantes por columna:")
print(faltantes_porcentaje)

# Eliminar filas que tengan al menos un valor faltante
df_sin_filas_faltantes = df.dropna()
print("\nDataFrame después de eliminar filas con valores faltantes:")
print(df_sin_filas_faltantes)

# Mostrar resumen de los datos restantes
print("\nInformación después de eliminar filas con valores faltantes:")
print(df_sin_filas_faltantes.info())

# Eliminar columnas que tengan al menos un valor faltante
df_sin_columnas_faltantes = df.dropna(axis=1)
print("\nDataFrame después de eliminar columnas con valores faltantes:")
print(df_sin_columnas_faltantes)

# Mostrar resumen de las columnas restantes
print("\nColumnas restantes después de eliminar columnas con valores faltantes:")
print(df_sin_columnas_faltantes.columns)

# Eliminar filas únicamente si todos los valores de la fila están faltantes
df_sin_filas_completamente_faltantes = df.dropna(how='all')
print("\nDataFrame después de eliminar filas con todos los valores faltantes:")
print(df_sin_filas_completamente_faltantes)

# Mostrar información sobre el DataFrame resultante
print("\nInformación después de eliminar filas con todos los valores faltantes:")
print(df_sin_filas_completamente_faltantes.info())

# 8.	Manejo de datos duplicados, que se presenten en la tabla Clientes
# Identificar filas duplicadas
duplicados = df.duplicated()
print("\nFilas duplicadas en la tabla Clientes (True indica duplicado):")
print(duplicados)

# Contar la cantidad de filas duplicadas
cantidad_duplicados = duplicados.sum()
print(f"\nCantidad de filas duplicadas: {cantidad_duplicados}")

# Filtrar y mostrar las filas duplicadas
filas_duplicadas = df[df.duplicated()]
print("\nFilas duplicadas encontradas:")
print(filas_duplicadas)

# Eliminar filas duplicadas y conservar la primera aparición
df_sin_duplicados = df.drop_duplicates()
print("\nDataFrame después de eliminar filas duplicadas:")
print(df_sin_duplicados)

# Mostrar la cantidad de filas restantes
print(f"\nCantidad de filas después de eliminar duplicados: {len(df_sin_duplicados)}")

# Eliminar duplicados considerando únicamente las columnas 'Nombre' y 'Telefono'
df_sin_duplicados_especificos = df.drop_duplicates(subset=['Nombre', 'Telefono'])
print("\nDataFrame después de eliminar duplicados basados en 'Nombre' y 'Telefono':")
print(df_sin_duplicados_especificos)

# Guardar las filas duplicadas en un archivo Excel para análisis
filas_duplicadas.to_excel('duplicados_clientes.xlsx', index=False)
print("\nDuplicados guardados en 'duplicados_clientes.xlsx'")

# 9.	Aplicar  transformaciones numéricas
# Normalizar la columna 'Edad' entre 0 y 1
scaler = MinMaxScaler()
df['Edad_Normalizada'] = scaler.fit_transform(df[['Edad']])
print("\nColumna 'Edad' Normalizada:")
print(df[['Edad', 'Edad_Normalizada']])

# Estandarizar la columna 'Edad'
scaler = StandardScaler()
df['Edad_Estandarizada'] = scaler.fit_transform(df[['Edad']])
print("\nColumna 'Edad' Estandarizada:")
print(df[['Edad', 'Edad_Estandarizada']])

# Aplicar la raíz cuadrada a la columna 'Edad' (donde no hay valores faltantes)
df['Raiz_Edad'] = df['Edad'].apply(lambda x: np.sqrt(x) if pd.notnull(x) else np.nan)
print("\nColumna 'Raiz_Edad':")
print(df[['Edad', 'Raiz_Edad']])

# Crear rangos de edad
bins = [0, 18, 35, 50, 100]
labels = ['Joven', 'Adulto Joven', 'Adulto', 'Mayor']
df['Categoria_Edad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)
print("\nCategorías de Edad:")
print(df[['Edad', 'Categoria_Edad']])

# Rellenar valores faltantes en 'Edad' con la mediana
df['Edad_Rellenada'] = df['Edad'].fillna(df['Edad'].median())
print("\nColumna 'Edad' Rellenada con la Mediana:")
print(df[['Edad', 'Edad_Rellenada']])

# Aplicar logaritmo natural a la columna 'Edad' (donde no hay valores faltantes)
df['Log_Edad'] = df['Edad'].apply(lambda x: np.log(x) if pd.notnull(x) and x > 0 else np.nan)
print("\nColumna 'Log_Edad':")
print(df[['Edad', 'Log_Edad']])

# Obtener estadísticas de 'Edad'
print("\nEstadísticas de la columna 'Edad':")
print(df['Edad'].describe())

# Sumar todas las edades (ignorando valores faltantes)
suma_edades = df['Edad'].sum(skipna=True)
print(f"\nSuma de todas las edades: {suma_edades}")

