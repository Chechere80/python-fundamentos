"""
#Ejercicio 7

Mostrar:

Promedio general.
Mejor estudiante.
Cantidad de aprobados.

estudiantes = [
    {"nombre":"Juan","nota":4.5},
    {"nombre":"Ana","nota":3.8},
    {"nombre":"Pedro","nota":4.9}
]

largo = int(len(estudiantes)) #requerida para calcular el promedio

nota = 0
nota_mas_alta = 0
aprobados = 0

for i in range(0,largo):
    nota += estudiantes[i]['nota']  # requerida para calcular el promedio
    if estudiantes[i]['nota'] > nota_mas_alta:
        nota_mas_alta = estudiantes[i]['nota']
        mejor_estudiante = estudiantes[i]['nombre']

    if estudiantes[i]['nota'] >= 3:
        aprobados += 1


promedio = round(nota/largo,1)

print(f'El promedio de las notas fue: {promedio}')
print(f'El mejor estudiante fue: {mejor_estudiante}')
print(f'La cantidad de estudiantes aprobados fue: {aprobados}')
"""
"""
#Ejercicio 8

Registrar varias ventas:
Guardar todas en una lista.

Después calcular:

Total vendido. OK
Venta más alta. 
Promedio de ventas.
Cliente con la venta más alta.
"""

ventas =\
[
{"cliente": "José", "valor": 250000},
{"cliente": "Pedro", "valor": 500000},
{"cliente": "Carlos", "valor": 750000}
]

total_ventas = 0
venta_mas_alta = 0
largo = int(len(ventas))


for i in range(0,largo):
    total_ventas += ventas[i]['valor']  # requerida para calcular el promedio

    if ventas[i]['valor'] > venta_mas_alta:
        venta_mas_alta = ventas[i]['valor']
        mejor_venta = ventas[i]['cliente']

print(f'La venta total fue de {total_ventas}')
print(f'La venta más alta fue de {venta_mas_alta}')
print(f'El promedio de ventas es de {round(total_ventas/largo,1)}')
print(f'La mejor venta fue de {mejor_venta}')









