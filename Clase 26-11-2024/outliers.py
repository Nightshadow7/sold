import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Supongamos que tienes un DataFrame llamado 'df'
# Ejemplo de datos
data = {'Edad': [18, 22, 25, 29, 34, 40, 120, 21, 28, 30]}
df = pd.DataFrame(data)

# Calcular Q1, Q3 y el IQR
Q1 = df['Edad'].quantile(0.25)
Q3 = df['Edad'].quantile(0.75)
IQR = Q3 - Q1

# Definir límites inferior y superior
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Identificar outliers
outliers = df[(df['Edad'] < limite_inferior) | (df['Edad'] > limite_superior)]
print("Outliers detectados:")
print(outliers)

# Eliminar los Outliers
# Filtrar datos sin outliers
df_sin_outliers = df[(df['Edad'] >= limite_inferior) & (df['Edad'] <= limite_superior)]
print("\nDataFrame sin outliers:")
print(df_sin_outliers)

# 3. Transformar los outliers:
# Una alternativa a eliminarlos es transformarlos, por ejemplo, reemplazarlos con el límite superior o inferior.
# Reemplazar valores menores al límite inferior por el límite inferior
# y valores mayores al límite superior por el límite superior
df_transformado = df.copy()
df_transformado['Edad'] = df['Edad'].apply(lambda x: limite_inferior if x < limite_inferior else (limite_superior if x > limite_superior else x))
print("\nDataFrame con outliers transformados:")
print(df_transformado)

# Visualización de Outliers 

# Antes de manejar los outliers
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Edad'])
plt.title("Antes de manejar los outliers")
plt.show()

# Después de eliminarlos
plt.figure(figsize=(10, 5))
sns.boxplot(x=df_sin_outliers['Edad'])
plt.title("Después de eliminar los outliers")
plt.show()
