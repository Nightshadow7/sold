# Importar las librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Cargar los datos desde un archivo Excel
df = pd.read_excel(r'C:\Users\herna\Music\Ciencia de datos\clase 18-11-2024\MORTALIDAD.xlsx', sheet_name='MORTALIDAD')

# Selección de la columna que se desea analizar, aquí se usa 'Edad Fallecido' como ejemplo
columna = 'Edad Fallecido'

# Calcular medidas de tendencia central
media = df[columna].mean()
mediana = df[columna].median()
moda = df[columna].mode()[0]

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Calcular medidas de dispersión
varianza = df[columna].var()
desviacion_estandar = df[columna].std()

print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")

# Gráfico de barras
sns.countplot(x=columna, data=df)
plt.title("Gráfico de barras")
plt.show()

# Gráfico de líneas
df[columna].plot(kind='line')
plt.title("Gráfico de líneas")
plt.show()

# Gráfico de pastel (pie chart)
df[columna].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Gráfico de pastel")
plt.show()

# Histograma
df[columna].plot(kind='hist', bins=20)
plt.title("Histograma")
plt.show()

# Diagrama de dispersión (scatter plot)
plt.scatter(df['Edad Fallecido'], df['DIAS OPORTUNIDAD'])
plt.xlabel('Edad Fallecido')
plt.ylabel('Días de Oportunidad')
plt.title("Diagrama de dispersión")
plt.show()

# Boxplot
sns.boxplot(x=columna, data=df)
plt.title("Boxplot")
plt.show()

# Mapa de calor (heatmap)
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title("Mapa de calor")
plt.show()

