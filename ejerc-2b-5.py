'''
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
una mayúscula o una minúscula.'''
# Introducir una letra
letra = input("Letra: ")
letras_minusculas = "abcdefghijklmnñopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
# Comprobar si es mayúscula o minúscula
if letra in letras_mayusculas:
    print(f"La letra {letra} esta en mayúscula")
elif letra in letras_minusculas:
    print(f"La letra {letra} esta en minúsculas")
else:
    print("¡Usted no ingreso una letra")