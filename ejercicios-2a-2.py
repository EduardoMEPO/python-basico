'''
CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla
'''
# Ingreso de contraseña
password = input("Password: ")

#1. La contraseña debe de tener:
# 1 vocal en minúsculas y 2 simbolos especiales diferentes (* o #)
if ("a" in password or "e" in password or "i" in password or "o" in password or "u" in password) and ("*" in password and "#" in password):
    # Indicar por pantalla si es segura la contraseña
    print("La contraseña es segura")
else:
    # Indicar por pantalla si no es segura la contraseña
    print("La contraseña no cumple con los requisitos de seguridad")