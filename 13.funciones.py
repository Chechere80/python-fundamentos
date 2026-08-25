'''
def sumar(a,b):
    return a + b

a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
print(f'La suma es: {sumar(a,b)}')
'''

def es_par(numero):
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')

    print('Gracias por usar nuestos servicios \n¡Vuelva pronto!')


numero = int(input("Ingrese un numero: "))

es_par(numero)




