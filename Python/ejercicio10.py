"""Escribir un algoritmo que convierta una cantidad de minutos a horas y minutos. 
El usuario debe ingresar la cantidad de minutos. """

print("""-------------------------------------------------------
                EJERCICIO 10: MINUTOS A HORAS
-------------------------------------------------------""")

minutos = int(input("Ingrese la cantidad de minutos a convertir: "))
horas = int(minutos/60)
minutosSobrantes = int(minutos%60)

print(f"La cantidad ingresada corresponde a {horas} horas y {minutosSobrantes} minutos")