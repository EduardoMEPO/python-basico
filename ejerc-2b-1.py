'''
EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla.
'''
# Ingreso de 4 números diferentes
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))
num4 = int(input("Cuarto número: "))
mayor = 0
# Encontrar el mayor de los números
if num1 > mayor:
    mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
if num4 > mayor:
    mayor = num4
# Imprimir el mayor
print(f"El número mayor es {mayor}.")