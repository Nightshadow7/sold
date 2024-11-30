import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo con 100 registros
data = {
  'Día': pd.date_range(start='2024-01-01', periods=100, freq='D'),  # Fechas diarias
  'Valor': [i * 0.5 + (i%5) for i in range(1, 101)]  # Valores con una tendencia lineal y algo de variabilidad
}

df = pd.DataFrame(data)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Configuración para la visualización
plt.figure(figsize=(10, 6))  # Tamaño de la figura

# Crear el gráfico de líneas
plt.plot(df['Día'], df['Valor'], marker='o', color='b', label='Valor', linestyle='--', markersize=4)

# Títulos y etiquetas de los ejes
plt.title('Gráfico de Líneas de Valor por Día')
plt.xlabel('Día')
plt.ylabel('Valor')

# Añadir leyenda
plt.legend()

# Rotar las etiquetas del eje X para facilitar su lectura
plt.xticks(rotation=45)

# Ajustar la visualización para evitar que se corten las etiquetas
plt.tight_layout()

# Mostrar el gráfico
plt.show()