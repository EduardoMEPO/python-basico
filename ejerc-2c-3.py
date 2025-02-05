'''
RESTAURANTE ONLINE:
En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
ingredientes.'''
# Elegir que tipo de hamburguesa quiere
hamburguesa = int(input("¿Qué tipo de hamburguesa desea? 1)Clasica - 2)Vegana : "))
ingrediente_extra = 0
if hamburguesa == 1:
    # Mostrar los ingredientes extras disponibles
    # Permitir escoger uno de ellos
    ingrediente_extra = int(input("Ingredientes extra \n1)Queso Idiazabal \n2)Bacon \n3)Huevo) \nque desea añadir: "))
    if ingrediente_extra == 1:
        # Imprimir tipo de hamburguesa y sus ingredientes
        print("Hamburguesa Clásica con Queso Idiazabal")
    elif ingrediente_extra == 2:
        # Imprimir tipo de hamburguesa y sus ingredientes
        print("Hamburguesa Clásica con Bacon")
    elif ingrediente_extra == 3:
        # Imprimir tipo de hamburguesa y sus ingredientes
        print("Hamburguesa Clásica con Huevo")
    else:
        # Imprimir tipo de hamburguesa y sus ingredientes
        print("Hamburguesa Clásica.")
elif hamburguesa == 2:
    # Mostrar los ingredientes extras disponibles
    # Permitir escoger uno de ellos
    ingrediente_extra = int(input("Ingredientes extra \n1)Tofu \n2)Cebolla caramelizada \nque desea añadir: "))
    if ingrediente_extra == 1:
        # Imprimir tipo de hamburguesa y sus ingredientes
        print("Hamburguesa Vegana con Tofu")
    elif ingrediente_extra == 2:
        # Imprimir tipo de hamburguesa y sus ingredientes
        print("Hamburguesa Vegana con Cebolla caramelizada")
    else:
        print("Hamburguesa Vegana.")
else:
    print("Opción invalida.")