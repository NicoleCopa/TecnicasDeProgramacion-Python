"""
Escribir un algoritmo que permita al usuario ingresar 2 números y luego le indique el 
resultado de la suma de esos dos números.
_______________________________________
ENTRADA                 IDENTIFICADOR
    Numero 1                num1
    Numero 2                num2
SALIDA
    Suma                    sum
_______________________________________
"""

#Decoracion: Nombre del algorítmo
print("-------------------------------------------------------")
print("           EJERCICIO 1: CALCULAR SUMA.")
print("-------------------------------------------------------")

#Entrada
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))

#Proceso
sum = num1 + num2

#Salida
print("El resultado de ambos números es:", sum)

"""
-------------------------------------------------------
            EJERCICIO 1: CALCULAR SUMA
-------------------------------------------------------
Ingrese un número: 20
Ingrese un segundo número: 10
El resultado de ambos números es: 30
"""