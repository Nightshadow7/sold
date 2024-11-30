import math as mt

# definicion de funciones 
def saludar(nombre):
  print(f"Hola, {nombre}!")
  
def calcular_area_circulo(radio):
  return mt.pi * radio ** 2

# funcion principal
def main():
  # variables y entrada de datos
  nombre_usuario = input("¿Como te llamas? ")
  saludar(nombre_usuario)

  try:
    radio = float(input("Ingresa el radio de un circulo: "))
    area = calcular_area_circulo(radio)
    print(f"El radio del circulo es: {area:.2f}")
  except ValueError:
    print("Por favor, ingresa un numero valido para el radio.")

# ejecutar el programa
if __name__ == "__main__":
  main()