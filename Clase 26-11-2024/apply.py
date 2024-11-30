import pandas as pd

# Ejemplo 1: Aplicar una función a cada elemento de una columna

# Crear un DataFrame
data = {'Edad': [18, 25, 30, 40, 50]}
df = pd.DataFrame(data)

# Aplicar una función lambda para categorizar las edades
df['Categoria'] = df['Edad'].apply(lambda x: 'Joven' if x < 30 else 'Adulto')
print("\nCategorizar edades con apply():")
print(df)
# Resultado: Se agrega una columna Categoria con valores Joven o Adulto.


# Ejemplo 2: Aplicar una función por fila
# Crear un DataFrame
data = {'Nombre': ['Ana', 'Luis'], 'Edad': [18, 25]}
df = pd.DataFrame(data)

# Concatenar nombre y edad por fila
df['Descripcion'] = df.apply(lambda row: f"{row['Nombre']} tiene {row['Edad']} años", axis=1)
print("\nDescripción con apply():")
print(df)
# Resultado: Se agrega una columna Descripcion con frases como: "Ana tiene 18 años".

