""". Se necesita un algoritmo que permita al usuario ingrese un número e informe 
si el mismo es PAR o IMPAR (ver operador mod)."""

print("""-------------------------------------------------------
                EJERCICIO 18: NÚMERO PAR Ó IMPAR
-------------------------------------------------------""")

num = int(input("Ingrese un número: "))

if num%2 == 0:
    print("El número es PAR.")
else:
    print("El número es IMPAR.")
    