'''
Escribe un programa que solicite tu nombre completo, el nombre de las cinco materias y la calificación
de cada una. Y como resultado devuelve tu nombre y el promedio obtenido en el semestre.
'''

materias = int(input("Ingrese el número de materias: "))
contador = 0
acumulado = 0
mejor_nota = 0

nombre_estudiante = input("Ingrese el nombre del estudiante: ")

while contador < materias:
    nombre_materia = input("Ingrese el nombre del materia: ")
    nota_materia = float(input("Ingrese la nota: "))
    if nota_materia > mejor_nota:
        mejor_nota = nota_materia
        mejor_materia = nombre_materia

    acumulado += float(nota_materia)
    contador += 1

promedio = round(float(acumulado/materias),1)

if promedio >= 3:
    print(f'El estudiante {nombre_estudiante} ha aprobado este semestre con un promedio de {promedio} '
          f'y la mejor nota es {mejor_nota} de la materia {mejor_materia}.')
else:
    print(f'El estudiante {nombre_estudiante} ha reprobado este semestre con un promedio de {promedio}.')




