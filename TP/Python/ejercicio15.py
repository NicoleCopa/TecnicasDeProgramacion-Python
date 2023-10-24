"""Escribir un algoritmo que permita al usuario ingresar un número e informe 
si el mismo es PAR (operador mod)."""

print("""-------------------------------------------------------
                EJERCICIO 15: NÚMERO PAR
-------------------------------------------------------""")

num = int(input("Ingrese un número: "))

if num%2 == 0:
    print("El número es par.")
    