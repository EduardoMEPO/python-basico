'''
DIVISION:
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
divisor es cero el programa debe mostrar un error.
'''
# Ingresar dos números
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
# Si el divisor es 0 debe mostrar error
if numero_dos == 0:
    print("¡Error!")
else:
    # Muestre por pantalla su división
    print(f"La división de los números es: {numero_uno/numero_dos}")