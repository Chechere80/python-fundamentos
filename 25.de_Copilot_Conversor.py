#Convenciones monedas de cambio

#1 = COP
#2 = GBP
#3 = YUAN

tasas = {
    "USD" : {1: 3100,
             2: 0.76,
             3: 6.37},
    "EUR" : {1: 4000,
             2: 0.83,
             3: 6.93}
}

moneda_requerida = int(input("Ingrese la moneda que requiere:  \n 1. Dólar\n 2. Euro\n: "))
if moneda_requerida not in (1,2):
    print("Escoge la moneda correcta")
else:
    cantidad_requerida = float(input("Ingrese la cantidad requerida: "))
    moneda_actual = int(input("Ingresa a la moneda que quieres convertir: \n1. COP\n2. GBP\n3. Yuan: "))
    if moneda_requerida == 1:
        dolar = round(cantidad_requerida * tasas["USD"][moneda_actual],2)
        print(f'La cantidad que requieres es de {dolar}')
    else:
        euro = round(cantidad_requerida * tasas["EUR"][moneda_actual],2)
        print(f'La cantidad que requieres es de {euro}')