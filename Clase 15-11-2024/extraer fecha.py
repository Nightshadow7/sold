# Escriba un programa que reciba la fecha en formato 'dd/mm/aaaa' como cadena y extraiga el año de la fecha

# Defino la fecha en formato 'dd/mm/aaaa'
fecha = "25/12/2023"

# Extraigo el año
año = fecha.split("/")[-2]

print(f"El año de la fecha {fecha} es: {año}")