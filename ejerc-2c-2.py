'''
Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
al mes. Además los tramos impositivos de la renta anual son los siguientes:
RENTA
TIPO IMPOSITIVO
Menos de 15.000 eu
5%
Entre 15.000 y 25.000 eu
15%
Entre 25.000 y 35.000 eu
20%
Entre 35.000 y 60.000 eu
30%
Más de 60.000 eu
45%
Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.'''
edad = int(input("Edad: "))
sueldo = float(input("Sueldo: "))
sueldo_anual = 0
# Verificar mayor de edad
# Verificar sueldo > 1000 euros
if edad >= 18 and sueldo > 1000:
    sueldo_anual = sueldo * 12
    # Verificar Tipo de Impositivo
    if sueldo_anual < 15000:
        print("Impositivo del 5%")
    elif sueldo_anual >= 15000 and sueldo_anual < 25000:
        print("Impositivo del 15%")
    elif sueldo_anual >= 25000 and sueldo_anual < 35000:
        print("Impositivo del 20%")
    elif sueldo_anual >= 35000 and sueldo_anual <= 60000:
        print("Impositivo del 30%")
    else:
        print("Impositivo del 45%")
else:
    print("No cumple con uno o los dos requisitos.")