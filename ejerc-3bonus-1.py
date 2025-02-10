'''
MATRIZ:
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1.
La fila cuyos elementos suman el máximo
2.
La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos)
'''
# Definir la lista
M = [[2,5,3],
     [6,1,8],
     [7,5,4]]

# Verificar si la M es una matriz
n_columanas = len(M[0])
n_filas = len(M)
es_matriz = True

# Recorrer todas las listas dentro de M (todas las filas de M)
for i in range(0, n_filas):
    # compruebo si la fila i tiene la misma dimensión
    # que la de referencia
    if len(M[i]) != n_columanas: # si no tiene el mismo número de columnas
        es_matriz = False # si alguna fila no tiene la misma longitud
                          # que la de referencia es_matriz sera Falso
        break

# Parte 1 -- Calculamos fila con su máxima y la imprimimos
# Si es una matriz ejecutamos
if es_matriz == True:

    sum_max = 0 # inicializamos la variable de suma máxima

    # Recorremos las filas con un bucle
    for i in range(0, n_filas):
        fila = M[i] # cada una de las filas
        suma_fila = sum(fila) # calculamos la suma de la fila

        # Comprobamos si la suma de la fila es mayor al de la fila anterior
        if suma_fila > sum_max:
            sum_max = suma_fila # actualizamos el valor de la suma maxima
            num_fila = i # actualizamos el valor del indice de la fila
                         # con la suma más alta
    
    print(f"La fila cuyos elementos suman el máximo es: {M[num_fila]} con una suma total de {sum_max}")

# Parte 2 -- Calculamos columna con su máximo y la imprimimos
# Ejecutamos solo si es una matriz
if es_matriz == True:
    sum_max = 0 # inicializamos la variable que gurada la suma máxima
    # recorrer todas las columnas de la matriz
    for j in range(0,n_columanas):
        columna = [] # inicializamos nuestra lista donde guardamos los valores
                     # de cada una de las columnas en cada iteración
        suma_columna = 0 # inicializamos la variable que contiene la suma de la columna

        # recorrer las filas de la matriz
        for fila in M:
            suma_columna = suma_columna + fila[j] # sumar cada elemento de la columna j
            columna.append(fila[j]) # añadir cada elemento de la columna j a nuestra columna
        
        # comprobar si la suma de la columna es mayor a la suma de la columna anterior
        if suma_columna > sum_max:
            sum_max = suma_columna # actualizamos el valor de la suma máxima
            columna_max = columna[:] # actualizamos el valor de la columna con suma máxima

    print(f"La columna cuyos elementos suman el máximo es: {columna_max} con una suma total de {sum_max}")