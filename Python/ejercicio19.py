"""Se necesita un algoritmo que permita al usuario el ingreso de dos números e 
informe al usuario si el primer número ingresado es mayor al segundo, si la situación 
es al revés o si son iguales."""

print("""-------------------------------------------------------
                EJERCICIO 19: MAYOR, MENOR O IGUAL
-------------------------------------------------------""")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    print(f"{num1} es mayor a {num2}.")
elif num1 < num2:
    print(f"{num1} es menor a {num2}.")
else:
    print("Ambos números son iguales.")