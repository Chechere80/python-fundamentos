def reporte_estudiante(*notas):
    total = 0
    cantidad = 0

    for nota in notas:
        total += nota

    cantidad = len(notas)

    #print(f' control {total}')

    nota_alta = max(*notas)
    nota_baja = min(*notas)
    print(f'La nota más alta fue {nota_alta}, '
          f'la nota mas baja fue {nota_baja} '
          f'y la cantidad de notas fue de {cantidad}\n')

    promedio = round(total / len(notas),1)

    print("Calculando promedio...")
    print("...")
    print(f'El promedio de las notas fue: {promedio}')


reporte_estudiante(4,3.7,5)




