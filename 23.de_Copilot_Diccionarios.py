"""trabajar = 1
while trabajar == 1:
    print("Acá funciona while")
    x = int(input("Introduce un numero:\n1. Seguir\n2. Salir \n: "))
    if x == 1:
        trabajar = True
    else:
        trabajar = False
        print("Saliste")

#Ejercicio 5
agenda = {"José": 302944, "Mario": 829455, "Ángel": 829405, "Luís": 930594}

print("\nBienvenido a tu agenda telefónica\n"
        "_________________________________\n")
print("\nIngrese la acción que requieres: \n")

trabajar = True

while trabajar:
    accion = int(input("\n1. Agregar contactos\n2. Consultar contactos\n3. Eliminar contactos\n"
                       "4. Salir\n--> "))

    if accion == 1:
        nombre = input("Ingrese nombre: ")
        if nombre not in agenda:
            numero = int(input("Ingrese numero: "))
            agenda[nombre] = numero
        else:
            print("Nombre ya está en la agenda")

    elif accion == 2:
        nombre = input("Ingrese nombre: ")
        if nombre in agenda:
            print("El nombre está en la agenda")
        else:
            print("El nombre no está en la agenda")
    elif accion == 3:
        nombre = input("Ingrese nombre: ")
        if nombre in agenda:
            agenda.pop(nombre)
        else:
            print("El nombre no está en la agenda")
    if accion == 4:
        trabajar = False
        print("Gracias por usa nuestro servicio.\nLa agenda ha finalizado")

    print(agenda)
#print("Gracias por utilizar la agenda")
"""

#Ejercicio 6:
mensaje1 = "El articulo no existe en el inventario\n"
inventario = {
    "Mouse": 15,
    "Teclado": 8,
    "Monitor": 4
}

#Consultar stock
consultar = True
print("\nBienvenido al inventario\n"
          "========================\n")

while consultar:

    accion = int(input("¿Que desea hacer?\n1. Consultar\n2. Modificar\n3. Añadir\n4. Salir\n--> "))

    if accion == 1:
        articulo = input("Ingresa el producto a buscar: ")
        if articulo in inventario:
            print(f'Existen {inventario[articulo]} unidades de {articulo}\n')
        else:
            print(mensaje1)

    elif accion == 2:
        articulo = input("Ingresa el producto a modificar el stock: ")
        if articulo in inventario:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            inventario[articulo] = nuevo_stock
            print(inventario)
        else:
            print(mensaje1)

    elif accion == 3:
        articulo = input("Ingresa el producto a ingresar en el inventario: ")
        if articulo not in inventario:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            inventario[articulo] = nuevo_stock
            print(inventario)
        else:
            print("El articulo ya existe en el inventario\n")
    if accion == 4:
        consultar = False
        print("Gracias por usa nuestro servicio.\nEl programa inventario ha finalizado")









