'''
NUMEROS PRIMOS 1:
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo.
'''
lista = list(range(2,101))
lista_primos = []
contador = 0

# verificar que no tiene mas de un divisor
for numero in lista:
    contador = 0
    for i in range(1,101):
        if numero % i == 0:
            contador += 1
    if contador == 2:
                lista_primos.append(numero)

print(lista_primos)