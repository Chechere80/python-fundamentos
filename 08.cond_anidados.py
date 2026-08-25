'''
diseño de programa que pide la edad y el estado de graduación
posibilidades
1. mayor de edad y graduado
2. mayor de edad y no graduado
3. menor de edad y graduado
4. menor de edad y no graduado

generar mensajes para cada combinación de resultados
'''

a = "Felicitaciones, ya eres mayor de edad"
b = "Felicidades, ya te graduaste"
c = "Aún no eres mayor de edad"
d = "Falta poco para tu grado"

edad = int(input("Ingresa tu edad: "))
grado = input("¿Ya terminaste tu estudio (si) (no): ")

if int(edad) > 18 and grado == "si":
    print(a, b)
if edad > 18 and grado == "no":
    print(a, d)
if edad < 18 and grado == "si":
    print (c, b)
if edad < 18 and grado == "no":
    print(c, d)