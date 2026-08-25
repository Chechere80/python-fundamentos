tupla1 = (0,1,1,2,3,5,8,13,21,34,55,89)

numero = int(input('Ingrese un numero: '))

conteo = tupla1.count(numero)

if conteo == 0:
    print(f'El numero {numero} no está en la tupla1')
elif conteo == 1:
    print(f'El número {numero} está 1 vez en la tupla1')
else:
    print(f'El número {numero} está {conteo} veces en la tupla1')

print("Gracias, vuelva pronto")