"""
Ejercicio 10. Ranking de estudiantes
Pide:
Nombre
Nota
para varios estudiantes.
Guárdalos en una lista de diccionarios.
Al final muestra:

🥇 Primer puesto
🥈 Segundo puesto
🥉 Tercer puesto

según la nota obtenida.
"""

lista1 = []

registro = True

while registro:
    accion = int(input("1. Registrar\n2. Terminar\n--> "))
    if accion not in (1, 2):
        print("Escoge la acción correcta")
    else:
        if accion == 1:
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            nota_estudiante = float(input("Ingrese la nota del estudiante: "))
            elemento = {"nombre": nombre_estudiante, "nota": nota_estudiante}
            lista1.append(elemento)
        else:
            registro = False

lista1.sort(key=lambda estudiante: estudiante["nota"], reverse=True)

print("El registro de estudiantes ha terminado.\n")

print(f'El primer puesto corresponde al estudiante {lista1[0]["nombre"]}, \n'
      f'el segundo puesto corresponde al estudiante {lista1[1]["nombre"]} y \n'
      f'el tercer puesto corresponde al estudiante {lista1[2]["nombre"]}.')






