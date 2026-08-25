'''#imprimir las letras de una palabra
palabra = input("Ingresa una palabra: ")

for i in palabra:
    print(i)


#Imprimir dando un rango numérico
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))

if a > b:
    for i in range(a):
        print(b+i)
elif b > a:
    for i in range(b):
        print(a+i)
else:
    print("Los números son iguales")

===================Ejercicio 1===================
#Crear variables iniciales
venta_total = 0
descuento_total = 0

#crear el ciclo para 5 clientes y pedir los datos de la operación
for i in range(5):
    nombre_cliente_ = input("Ingresa el nombre del cliente: ")
    valor_compra = float(input("Ingresa el valor del compra: "))

#Calcular los descuentos
    if valor_compra < 80:
        descuento = 0
    elif valor_compra < 150:
        descuento = valor_compra * 0.1
    elif valor_compra < 300:
        descuento = valor_compra * 0.15
    else:
        descuento = valor_compra * 0.20

    #hacer los cálculos
    venta_total += valor_compra
    descuento_total += descuento

#Calcula la venta final
venta_final = venta_total-descuento_total

print (f'El valor total de las ventas es de ${venta_total}; '
       f'el descuento otorgado fue por valor de ${descuento_total} ' 
       f'y la venta total luego de descuentos es de ${venta_final}')
'''


#===================Ejercicio 2===================#
notas_acumuladas = 0
estudiantes_aprobados = 0
mejor_nota = 0

numero_estudiantes = int(input("Ingresa el numero de estudiantes: "))

for _ in range(numero_estudiantes):
    nombre_estudiante = input("Ingresa el nombre del estudiante: ")
    nota_estudiante = float(input("Ingresa la nota del estudiante: "))

    if nota_estudiante >= 3:
        estudiantes_aprobados += 1

    notas_acumuladas += nota_estudiante

    if nota_estudiante > mejor_nota:
        mejor_nota = nota_estudiante

promedio = notas_acumuladas/numero_estudiantes

print(f'El promedio general del grupo es de {promedio:.1f}, '
      f'y aprobaron {estudiantes_aprobados} estudiantes. '
      f'La mejor nota del curso fue {mejor_nota}')


