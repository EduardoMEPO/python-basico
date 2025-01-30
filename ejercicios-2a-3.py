'''
PAR O IMPAR:
Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)
'''
# Dado un número y una potencia
numero = int(input("Número: "))
potencia = int(input("Potencia: "))

# Si el número es par: el resultado elevandolo a la potencia es par.
# Si el número es impar: el resultado elevandolo a la potencia es impar.
# Comprobar si el número elevado a esa potencia es par o impar
if numero % 2 == 0:
    print(f"El número {numero**potencia} es par.")
else:
    print(f"El número {numero**potencia} es impar.")