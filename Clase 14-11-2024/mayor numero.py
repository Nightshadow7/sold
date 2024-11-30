# Función para pedir un número y validarlo
def pedir_numero(mensaje):
  while True:
    try:
      numero = float(input(mensaje))
      return numero
    except ValueError:
      print("Error: por favor ingresa un número válido.")

# Pedir los tres números usando la función de validación
num1 = pedir_numero("Dijita el primer numero: ")
num2 = pedir_numero("Dijita el segundo numero: ")
num3 = pedir_numero("Dijita el tercer numero: ")

# Encontrar el mayor sin usar max()
if num1 > num2 and num1 > num3:
  mayor = num1
elif num2 > num1 and num2 > num3:
  mayor = num2
else:
  mayor = num3

print(f"El numero mayor es: {mayor}")

