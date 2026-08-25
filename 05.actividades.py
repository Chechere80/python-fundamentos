

#Pedir números al usuario

primer_numero = int(input("Ingresa un número (1): " )) #3
segundo_numero = int(input("Ingresa un número (2): " )) #4

# Ejercicio 1
print (f'la suma es: {primer_numero+segundo_numero}') #7
# Ejercicio 2
print (f'la multiplicación es: {primer_numero*segundo_numero}')  #12
# Ejercicio 3
if primer_numero == segundo_numero:
    print ("Los números son iguales")
elif (primer_numero > segundo_numero):
    print(f'El número {primer_numero} es mayor que {segundo_numero}')
else:
    print(f'El número {segundo_numero} es mayor que {primer_numero}')


'''
# Ejercicio 4
print (f'¿el primer número es menor que el segundo? {primer_numero<segundo_numero}') #True
# Ejercicio 5
print (f'¿El primer numero es mayor o igual al primero? {primer_numero>=segundo_numero}') #False
'''
