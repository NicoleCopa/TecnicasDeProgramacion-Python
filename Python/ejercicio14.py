"""Escribir un algoritmo que determine si un número es menor o mayor a otro."""

print("""-------------------------------------------------------
                EJERCICIO 14: NÚMERO MENOR
-------------------------------------------------------""")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    print(f"{num1} es mayor a {num2}")
else:
    print(f"{num1} es menor a {num2}")