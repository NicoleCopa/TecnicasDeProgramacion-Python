"""Escribir un algoritmo que calcule el promedio de tres notas ingresadas por el usuario."""

print("""-------------------------------------------------------
                EJERCICIO 5: PROMEDIO
-------------------------------------------------------""")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio de las notas ingresadas es {promedio}")
