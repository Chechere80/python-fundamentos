#ingrese números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo numero: "))

#operar e imprimir resultados
if int(a) > int(b):
    c = a-b
    print(f'El resultado es: {c}')
elif int(a) < int(b):
    c = b-a
    print(f'El resultado es: {c}')
else:
    print("Los números son iguales")




