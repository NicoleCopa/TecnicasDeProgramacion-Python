"""Escribir un algoritmo que permita al usuario ingresar un número, y en caso de que
este sea impar, se informe el resultado de ese número multiplicado por 2"""

print("""-------------------------------------------------------
                EJERCICIO 17: NÚMERO IMPAR
-------------------------------------------------------""")

num = int(input("Ingrese un número: "))

if num%2 != 0:
    impar = num * 2
    print(f"{num} x 2 = {impar}")
    
