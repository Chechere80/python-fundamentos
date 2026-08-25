'''
Diseño de programa que pide la edad y el estado de finalización de estudio.
Posibilidades:
1. mayor de edad y graduado
2. mayor de edad y no graduado
3. menor de edad y graduado
4. menor de edad y no graduado

generar mensajes para cada combinación de resultados
'''

a = "Felicitaciones, ya eres mayor de edad y"
b = "felicidades, ya te graduaste."
c = "Aún no eres mayor de edad y"
d = "falta poco para tu grado."

edad = int(input("Ingresa tu edad: "))
grado = input("¿Ya terminaste tu estudio (si) (no)?: ")

if edad >= 18:
    if grado == "si":
        print(a,b)
    else:
        print(a,d)
if edad < 18:
    if grado == "no":
        print(c,d)
    else:
        print(c,b)

print("Mil gracias por participar.")