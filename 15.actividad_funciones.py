def conversor(moneda_actual, valor_moneda_actual, moneda_convertir):

    if moneda_actual == 1:
        #def a_dolar():
            if moneda_convertir == 1:
                print(f'Si necesitas USD{valor_moneda_actual} equivalen a ${valor_moneda_actual * 3750}')
            elif moneda_convertir == 2:
                print(f'Si necesitas USD{valor_moneda_actual} equivalen a ¥{valor_moneda_actual * 6.37}')
            elif moneda_convertir == 3:
                print(f'Si necesitas USD{valor_moneda_actual} equivalen a £{valor_moneda_actual * 0.76}')
            else:
                print("No se reconoce la moneda que requieres")

        #a_dolar()

    elif moneda_actual == 2:
        #def a_euro():
            if moneda_convertir == 1:
                print(f'Si necesitas EUR{valor_moneda_actual} equivalen a ${valor_moneda_actual * 4000}')
            elif moneda_convertir == 2:
                print(f'Si necesitas EUR{valor_moneda_actual} equivalen a ¥{valor_moneda_actual * 6.93}')
            elif moneda_convertir == 3:
                print(f'Si necesitas EUR{valor_moneda_actual} equivalen a £{valor_moneda_actual * 0.83}')
            else:
                print("No se reconoce la moneda que requieres")

        #a_euro()
    else:
        print("No se reconoce la moneda que tienes")


moneda_actual = int(input("Ingresa la moneda actual: \n 1. Dólar\n 2. Euro\n: "))
valor_moneda_actual = int(input("Ingresa la cantidad necesitada: "))
moneda_convertir =int((
        input("Ingresa la moneda a la que quieres convertir: \n 1. COP\n 2. Yuan\n 3. GBP\n: ")))


conversor(moneda_actual, valor_moneda_actual, moneda_convertir)
