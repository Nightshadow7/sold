# Importar las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Crear un conjunto de datos de ejemplo (puedes usar tus propios datos)
# Por ejemplo, 'X' podría representar el número de horas estudiadas, y 'y' el puntaje obtenido en un examen.
data = {
  'Horas Estudio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  'Puntaje Examen': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

# Convertir el diccionario en un DataFrame de pandas
df = pd.DataFrame(data)

# Visualizar los primeros registros del DataFrame
print(df.head())

# Separar las variables predictoras (X) y la variable objetivo (y)
X = df[['Horas Estudio']]  # Características (independientes)
y = df['Puntaje Examen']   # Variable objetivo (dependiente)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
regressor = LinearRegression()

# Entrenar el modelo usando el conjunto de entrenamiento
regressor.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = regressor.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Imprimir los resultados
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
print(f'R2 Score: {r2}')

# Visualizar los resultados en un gráfico
plt.scatter(X_test, y_test, color='blue', label='Datos Reales')  # Datos reales
plt.plot(X_test, y_pred, color='red', label='Predicción')  # Línea de predicción
plt.title('Regresión Lineal: Puntaje vs Horas de Estudio')
plt.xlabel('Horas de Estudio')
plt.ylabel('Puntaje en el Examen')
plt.legend()
plt.show()
