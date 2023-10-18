"""Escribir un algoritmo que convierta una temperatura en grados Celsius a Fahrenheit. 
El usuario debe ingresar la temperatura en grados Celsius. Para ello, deberá multiplicar 
la temperatura por 1.8 y sumarle 32 para obtener la temperatura en grados Fahrenheit."""

print("""-------------------------------------------------------
                EJERCICIO 3: CELCIUS A FAHRENHEIT
-------------------------------------------------------""")

celcius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celcius * 1.8) + 32

print(f"La temperatura en grados Fahrenheit es {fahrenheit}")
