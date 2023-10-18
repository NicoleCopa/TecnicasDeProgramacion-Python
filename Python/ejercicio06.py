"""Escribir un programa que convierta una cantidad de pesos argentinos a dólares 
estadounidenses(blue), utilizando un tipo de cambio fijo. 
El usuario debe ingresar la cantidad de pesos."""

print("""-------------------------------------------------------
                EJERCICIO 6: PESOS A DOLARES
-------------------------------------------------------""")

dolar = 985
pesos = float(input("Ingrese la cantidad de pesos a convertir: "))

conversion = dolar * pesos

print(f"La conversion de ${pesos} ARS a dolar es: ${conversion} USD")