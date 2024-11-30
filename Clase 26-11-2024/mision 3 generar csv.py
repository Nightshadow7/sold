import numpy as np
import random
from faker import Faker
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Inicializar Faker para generar datos ficticios
fake = Faker()

# Crear la estructura de la tabla 'terceros'
Base = {
  'Nombre': [],
  'Apellido': [],
  'Edad': [],
  'Telefono': [],
  'Ciudad': [],
  'Email': [],
  'Fecha_Registro': [],
  'Genero': [],
  'Ocupacion': [],
  'Comentarios': [],
}

# Opciones para datos repetidos
nombres_repetidos = ['Ana', 'Luis', 'Juan', 'María', 'Pedro']
ciudades_repetidas = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Granada']
emails_repetidos = ['ejemplo1@example.com', 'ejemplo2@example.com', 'ejemplo3@example.com']

# Opciones para géneros y ocupaciones
generos = ['Masculino', 'Femenino', 'Otro']
ocupaciones = ['Ingeniero', 'Profesor', 'Médico', 'Diseñador', 'Estudiante', 'Contador', 'Chef', 'Abogado', np.nan]

# Generar 50 registros ficticios
for _ in range(500000):
  Base['Nombre'].append(random.choice(nombres_repetidos) if random.random() > 0.2 else fake.first_name())
  Base['Apellido'].append(fake.last_name())
  Base['Edad'].append(random.choice([random.randint(18, 65), np.nan]))
  Base['Telefono'].append(fake.phone_number() if random.random() > 0.1 else np.nan)
  Base['Ciudad'].append(random.choice(ciudades_repetidas) if random.random() > 0.2 else np.nan)
  Base['Email'].append(random.choice(emails_repetidos) if random.random() > 0.3 else fake.email())
  Base['Fecha_Registro'].append(fake.date_between(start_date='-2y', end_date='today'))
  Base['Genero'].append(random.choice(generos))
  Base['Ocupacion'].append(random.choice(ocupaciones))
  Base['Comentarios'].append(fake.sentence() if random.random() > 0.3 else np.nan)

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(Base)

# Guardar en un archivo CSV si es necesario
df.to_excel('terceros.xlsx', index=False)
