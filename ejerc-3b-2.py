'''
NUMEROS PRIMOS 2:
Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados
'''
# Lista números enteros
lista_num = [2,3,4,5,6,11,13,15,23]
# Lista con los números primos de la lista original
lista_primos = []
# Número total de primos encontrados
num_primos = 0
# Suma de números primos
sum_primos = 0

# Identificar números primos
for num in lista_num:
    primo = True
    for i in range(2,num):
        if num % i == 0:
            primo = False
    if primo == True:
        # Agregar primos a la lista de primos
        lista_primos.append(num)
# Número total de primos
num_primos = len(lista_primos)
# Suma de lista_primos
sum_primos = sum(lista_primos)

print(lista_primos)
print(num_primos)
print(sum_primos)