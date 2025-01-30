'''
CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla
'''
contrasenia = input("Password: ")
contrasenia = contrasenia.replace(" ","")
print(contrasenia)