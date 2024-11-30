from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Edad': [18, 25, 30, 40, 50]}
df = pd.DataFrame(data)

# Aplicar MinMaxScaler
scaler = MinMaxScaler()
df['Edad_Normalizada'] = scaler.fit_transform(df[['Edad']])

print("\nEscalado con MinMaxScaler:")
print(df)

# Resultado: La columna Edad será transformada para estar en el rango [0, 1].