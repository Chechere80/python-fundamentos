#ingrese números
a = int(input("número 1: "))
b = int(input("numero 2: "))

#operar e imprimir resultados
if int(a) > int(b):
    c = a-b
    print(f'El resultado es: {c}')
elif int(a) < int(b):
    c = b-a
    print(f'El resultado es: {c}')
else:
    print("Los números son iguales")

    #print(f'El termino a evaluar: {a} es un dato de tipo: {type(a)}')


