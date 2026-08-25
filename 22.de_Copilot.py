"""
Solicita al usuario 5 notas y guárdalas en una lista.

Al final muestra:

La lista completa.
El promedio.
La nota más alta.
La nota más baja.
"""
notas = []


contador = 0
j = int(input("Ingrese cantidad de notas: "))

while j >= contador + 1:
    notas.append(float(input("Ingrese nota: ")))
    contador += 1

suma = 0
for i in notas:
    suma += float(i)

promedio = round(suma/len(notas),2)

print(f'Las notas del estudiante fueron: {notas}')
print(f'El promedio de las notas fue: {promedio}')
print("La nota más alta fue: " + str(max(notas)))
print("La nota más baja fue: " + str(min(notas)))


"""
#2

Pide 10 notas.

Recorre la lista y cuenta:

Cuántos aprobaron (>=3.0)
Cuántos reprobaron (<3.0)

notas = []

contador = 0
while contador <= 9:
    notas.append(float(input("Ingrese nota: ")))
    contador += 1

aprobaron = 0
reprobaron = 0
for i in notas:
    if i < 3.0:
        reprobaron += 1
    else:
        aprobaron += 1

print(f'\nEl número de estudiantes que aprobaron fue de {aprobaron}')
print(f'El número de estudiantes que reprobaron fue de {reprobaron}')
"""