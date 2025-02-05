## BUCLES:
'''
1.
Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
*
**
***
****
*****
****
***
**
*

# ingresar numero de estrellas en el medio
num_estrellas = int(input("Ingrese número de estrellas: "))
# Incrementamos hasta llegar al número de estrellas dado
for i in range(0,num_estrellas):
    i = i+1
    print("*"*i)
# Decrementamos las estrellas
for i in range(num_estrellas-1,0,-1):
    print("*"*i)
'''

'''
2.
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# almacenar cadena
caracteres = "contraseña"
contrasenia = input("Ingrese la contraseña: ")
while contrasenia != caracteres:
    print("Contraseña incorrecta, intente de nuevo.")
    contrasenia = input("Ingrese la contraseña: ")
print("Contraseña correcta. Bienvenido!!")
'''

'''
3.
Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última.

# Ingresar un palabra
palabra = input("Ingrese un palabra: ")
# Invertir palabra
long_palabra = len(palabra)
# Imprimir cada letra
for i in range(long_palabra-1,-1,-1):
    print(palabra[i])
'''

'''
4.
Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.
'''
# Ingresar frase
frase = input("Ingrese un frase: ")
# Ingresar Letra
letra = input("Ingrese una letra: ")
contador = 0
veces_vez = "vez"
for i in frase:
    if i == letra:
        contador+=1
        # Verificar si es vez o veces
        if contador > 1:
            veces_vez = "veces"
# número de veces que aparece la letra en la palabra
print(f"La letra {letra} se repite {contador} {veces_vez} en la frase {frase}")