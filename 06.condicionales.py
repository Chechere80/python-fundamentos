'''
¿Es mi computadora nueva o vieja?
La condición es que si tiene un tiempo t mayor a dos (2) años, es mayor
dato de entrada: fecha de compra
Respuestas posibles: tu computadora es nueva; tu computadora es vieja
'''

#ingresar dato
a = int(input('Introduce la fecha de compra de tu PC: '))
t = 2026-int(a)

#Evaluar las condiciones
if t < 0:
    print("Ingresa una fecha inferior a 2026")
elif t <2:
    print("Tu PC es nueva")
else:
    print("Tu PC es vieja")