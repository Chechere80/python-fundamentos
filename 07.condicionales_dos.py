'''
En una escuela de conducción, se otorgan licencias según la edad, que se puede agrupar en 4 categorías
cat1: si la edad es menor a 16 años, entonces no puede conducir
cat2: si la edad es menor a 18 años, entonces puede tener un permiso de conducción
cat3: si la edad es menor a 70 años, entonces puede tener una licencia estándar
cat4: si la edad es mayor a 70 años, entonces debe tener una licencia especial
'''
#Datos para evaluar
anio_actual = 2026
anio_nacimiento = int(input("Ingrese el anio de nacimiento: "))

edad = anio_actual - anio_nacimiento

if edad < 0:
    print(f'Tu edad no puede ser {edad}')
elif edad < 16:
    print(f'Tu edad es {edad} y no puedes conducir')
elif edad < 18:
    print(f'Tu edad es {edad} y puedes tener un permiso de conducción')
elif edad < 70:
    print(f'Tu edad es {edad} y puedes tener una licencia estándar')
else:
    print(f'Tu edad es {edad} y debes tener una licencia especial')

print("Gracias por usar nuestros servicios")

