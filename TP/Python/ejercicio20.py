"""Se requiere de un algoritmo que permita al usuario ingresar 3 números 
distintos e indique cuál de ellos es el mayor."""

print("""-------------------------------------------------------
                EJERCICIO 20: NÚMERO MAYOR
-------------------------------------------------------""")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))

if (num1 > num2) and (num1 > num3):
    print(f"El número {num1} es mayor")
elif (num2 > num3):
    print(f"El número {num2} es mayor")
else:
    print(f"El número {num3} es mayor")
    