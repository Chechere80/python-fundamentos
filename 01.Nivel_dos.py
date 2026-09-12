#Validador de edad para admisión

rechazo = "Por tu edad, no puedes ingresar acá"
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")

if int(edad) >= 18:
    print (f'Bienvenido, {nombre} {apellido}')
else:
    print(rechazo)

print("También vamos a probar los branches en git hub")