agenda = {"José": 302944, "Mario": 829455, "Ángel": 829405, "Luís": 930594}

print(type(agenda))

Acceso = int(input("Digite 1 para ingresar a la agenda o 2 para salir: "))

while Acceso == 1:

    nombre = str(input("Ingrese un nombre: "))

    if nombre in agenda:
        print(f'El nombre ya existe; el número de teléfono de {nombre} es el {agenda[nombre]}\n')
        eliminar = int(input("¿Desea eliminar este registro?\n1. Si\n2. No\n"))
        if eliminar == 1:
            agenda.pop(nombre)
        else:
            otro_numero = int(input("¿Desea ingresar un nuevo número de teléfono?\n1. Si\n2. No\n"))
            if otro_numero == 1:
                numero_nuevo = int(input("Ingrese un nuevo número: "))
                agenda[nombre] = numero_nuevo
    else:
        print(f'{nombre} no está en la agenda')
        nuevo_numero = int(input("Ingrese un nuevo número: "))
        agenda[nombre] = nuevo_numero

    print(agenda)
    Acceso = int(input("Digite 1 para ingresar a la agenda o 2 para salir: "))
