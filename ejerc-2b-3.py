'''
EL TRIÁNGULO:
En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
con esas piezas.
'''
# Ingresar las tres longitudes:
pieza1 = int(input("Longitud pieza 1: "))
pieza2 = int(input("Longitud pieza 2: "))
pieza3 = int(input("Longitud pieza 3: "))
# Condiciones para que el triángulo pueda formarse
# 1. Ninguna pieza puede ser 0.
if pieza1 > 0 and pieza2 > 0 and pieza3 > 0:
    # 2. La suma de dos piezas debe ser mayor que el trecero.
    if pieza1<(pieza2+pieza3) and pieza2<(pieza1+pieza3) and pieza3<(pieza1+pieza2):
        print(f"El triángulo si se puede construir con piezas de {pieza1}, {pieza2} y {pieza3}.")
    else:
        print(f"No es posible la construcción de un triangulo con las piezas de {pieza1}, {pieza2} y {pieza3}.")
else:
    print("¡Error! No existe una pieza que mida 0 cm.")