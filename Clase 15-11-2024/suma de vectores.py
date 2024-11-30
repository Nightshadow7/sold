# Crea dos listas que representen dos vectores y realiza la suma de estos vectores elemento por elemento
# sin usar librerias de numpy

# 2. Suma de vectores sin numpy
# Definir vectores
vector1 =[1 , 2 , 3]
vector2 =[4 , 5 , 6]

# Suma de vectores elemento por elemento
suma = [vector1[i] + vector2[i] for i in range(len(vector1))]
print(f"La suma de los vectores es: {suma}")