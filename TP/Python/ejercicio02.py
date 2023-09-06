"""
Escribir un algoritmo que intercambie dos valores ingresados por el usuario. 
Ejemplo: Si la variable num1 al inicio del algoritmo vale 5 y la variable num2 vale 10, 
al final del algoritmo num1 debe valer 10 y num2 5. 
_______________________________________
ENTRADA                 IDENTIFICADOR
    Numero 1                num1
    Numero 2                num2
SALIDA
    Número temporal         temp
_______________________________________
"""
#Decoracion: Nombre del algorítmo
print("-------------------------------------------------------")
print("         EJERCICIO 2: INTERCAMBIO DE NÚMEROS.")
print("-------------------------------------------------------")

#Entrada
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))

#Salida
temp = num1
num1 = num2
num2 = temp

print("El primer número es:", num1)
print("El segundo número es:", num2)

"""
-------------------------------------------------------
         EJERCICIO 2: INTERCAMBIO DE NÚMEROS
-------------------------------------------------------
Ingrese un número: 5
Ingrese un segundo número: 10
Primer número: 10
Segundo número: 5
"""