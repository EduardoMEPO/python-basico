'''
RELACION ENTRE NÚMEROS:
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos.
'''
# 3 números diferentes
print("Ingrese 3 números diferentes.")
print("")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))
# Verificar si son diferentes.
if num1 != num2 != num3:
    # Indicar si algun número es la suma de los otros dos.
    if num1 == (num2+num3):
        print(f"{num1} es la suma de {num2} + {num3}")
    if num2 == (num1+num3):
        print(f"{num2} es la suma de {num1} + {num3}")
    if num3 == (num1+num2):
        print(f"{num3} es la suma de {num1} + {num2}")
else:
    print("¡Error!. Los números deben de ser diferente")