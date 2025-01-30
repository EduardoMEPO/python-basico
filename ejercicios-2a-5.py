'''
LOG-IN:
Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
'''
# Ingrese una contraseña
password = input("Password: ")
# Contraseña
key = "contrasenia"
# No distinge entre mayúsculas y minúsculas.
password = password.lower()
# Si la contraseña es correcta, imprimir una bienvenida.
if password == key:
    print(f"¡Bienvenido Usuario!")
else:
    # Dar segunda oportunidad
    password = input("Segunda oportunidad, Password: ")
    # No distinge entre mayúsculas y minúsculas.
    password = password.lower()
    if password == key:
        print(f"¡Bienvenido Usuario!")
    else:
        # Al segundo fallo imprimir mensaje de error y terminar el programa.
        print("¡Error!")