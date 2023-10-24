"""Escribir un algoritmo que permita al usuario ingresar un numero e informe 
si el número ingresado es múltiplo de 6."""

print("""-------------------------------------------------------
                EJERCICIO 16: MÚLTIPLO DE 6
-------------------------------------------------------""")

num = int(input("Ingrese un número: "))

if (num%2 == 0) and (num%3 == 0):
    print("El número es múltiplo de 6.")
