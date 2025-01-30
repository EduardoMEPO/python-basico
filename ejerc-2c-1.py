'''
GRUPOS DE ALUMNOS:
En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
pantalla el grupo que le corresponde a ese alumno.'''
# Genero:
genero = input("Género: ")
genero = genero.lower()
# nombre:
nombre = input("Nombre: ")
# Existen 2 grupos "A" y "B"
chicasA = "EFGHIJKLM"
chicosA = "ABCDEFGHRSTUVXWYZ"
# "A" -> Chicas "E->M"          "A" -> Chicos "A->H y R->Z" 
# "B" -> Chicas "A->D y N->Z"   "B" -> Chicos "I->Q"
if genero == "mujer":
    if nombre[0].upper() in chicasA:
        # Imprimir el grupo que le corresponde a ese alumno
        print(f"La mujer {nombre} pertenece al grupo A")
    else:
        # Imprimir el grupo que le corresponde a ese alumno
        print(f"La mujer {nombre} pertenece al grupo B")
elif genero == "varon":
    if nombre[0].upper() in chicosA:
        # Imprimir el grupo que le corresponde a ese alumno
        print(f"El varón {nombre} pertenece al grupo A")
    else:
        # Imprimir el grupo que le corresponde a ese alumno
        print(f"El varón {nombre} pertenece al grupo B")
else:
    print("Género incorrecto.")