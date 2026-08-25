"""
#3
Crear una tupla
Mostrar los datos individualmente.
Después intenta obtener cada campo usando índices.
"""

estudiante = ("César",40,"Analista III")
print(type(estudiante))

print(estudiante)

nombre = (f'El nombre del estudiante es {estudiante[0]}')
edad = (f'La edad {estudiante[0]} es {estudiante[1]} años')
cargo = (f'Su cargo es {estudiante[2]}')

print(nombre)
print(edad)
print(cargo)

"""
#4
Guardar temperaturas de una semana

Mostrar:
Temperatura máxima.
Temperatura mínima.
Promedio.

"""
temperaturas = (22, 24, 25, 19, 23, 21, 26)

maxima = f'La temperatura máxima fue: {max(temperaturas)}'
minima = f'La temperatura mínima fue: {min(temperaturas)}'
promedio = f'El promedio de la temperatura fue: {round(sum(temperaturas)/len(temperaturas),2)}'

print(maxima)
print(minima)
print(promedio)
