"""Escribir un programa que calcule el área de un triángulo, dados su base y altura. 
El usuario debe ingresar la base y la altura."""

print("""-------------------------------------------------------
                EJERCICIO 4: AREA DE UN TRIÁNGULO
-------------------------------------------------------""")

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2

print(f"El area del triángulo es {area}")
