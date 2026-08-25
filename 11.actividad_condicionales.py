'''
Imagina que la tienda donde usted trabaja ofrece descuentos a los clientes en navidad,
de acuerdo con el monto de su compra.

Si es menor a 80, 0%
Si es mayor o igual a 80 y menor que 150, 10%
Si es mayor o igual a 150 y menor a 300, 15%
Si es mayor o igual a 300, 20%

Teniendo en cuenta la tabla, te piden que escribas un programa que solicite el nombre del cliente y
el valor de la compra. Y que arroje como resultado:

Nombre del cliente
Valor de la compra sin descuento
Valor de la compra con descuento.
'''

#Ingresar datos
nombre_cliente = input("Ingrese el nombre del cliente: ")
valor_compra = float(input("Ingrese el valor de la compra: "))

#Descuentos:
if valor_compra < 80:
    descuento = 0
elif valor_compra < 150:
    descuento = valor_compra*0.1
elif valor_compra < 300:
    descuento = valor_compra*0.15
else:
    descuento = valor_compra*0.20

valor_total = valor_compra - descuento

print(f'{nombre_cliente}, el valor de compra es ${valor_compra}, tu descuento es: '
      f'${descuento} y el valor total es: ${valor_total}')
