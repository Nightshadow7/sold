from sklearn.preprocessing import StandardScaler
import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Edad': [18, 25, 30, 40, 50]}
df = pd.DataFrame(data)

# Aplicar StandardScaler
scaler = StandardScaler()
df['Edad_Estandarizada'] = scaler.fit_transform(df[['Edad']])

print("\nEscalado con StandardScaler:")
print(df)

# Resultado: La columna Edad será transformada a valores con una media de 0 y desviación estándar de 1.