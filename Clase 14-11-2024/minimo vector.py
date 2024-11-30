# Dado un vector de numeros, encuentra manualmente el numero minimo en el vector 
# sin usar la funcion min(), imprementado tu propio bucle

# Definir el vector de numeros
vector=[]

for i in range(5):
  numero = float(input(f"Ingrese el numero {i+1}: "))
  vector.append(numero)

# Encontrar el minimo manualmente
minimo = vector[0]

for num in vector:
  if num < minimo:
    minimo = num
    
print(f"El numero minimo es: {minimo}")