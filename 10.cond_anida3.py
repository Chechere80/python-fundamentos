'''
Escribe un programa para evaluar el largo y la exactitud de la contraseña
Requisitos: largo de contraseña minimo 8 carácteres
Si la contraseña es menor a 8 carácteres, sacar un mensaje que lo exprese
si la contraseña pasa los 8 carácteres, validar que sea la correcta
'''

Contrasenia = input("Ingrese contraseña: ")

if len(Contrasenia) < 8:
    print("Contraseña no cumple con la cantidad mínima de caracteres")
else:
    if Contrasenia == "Prueba123":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")




