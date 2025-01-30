'''
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
'''
# Pide Nombre:
nombre = input("Nombre: ")
# Pide Edad:
edad = int(input("Edad: "))
# Promedio de Nota:
promedio = float(input("Promedio: "))
# Becas para promedio >= 8
# Y deben de tener 21 >= Edad >= 17
if promedio >= 8 and edad >= 17 and edad <= 21:
    # Indicar si puede optar por la beca o no.
    print(f"{nombre} puede obtar por una Beca.")
else:
    print(f"{nombre} no puede obtar por una Beca")