"""
Escribir un algoritmo que permita al usuario ingresar 2 números y luego le indique el 
resultado de la multiplicación entre esos dos números
_______________________________________
ENTRADA                 IDENTIFICADOR
    Primer número           num
    Segundo número          exp
SALIDA
    Multiplicación          mult
_______________________________________
"""

#Decoracion: Nombre del algorítmo
print("-------------------------------------------------------")
print("        EJERCICIO 5: CÁLCULO DE MULTIPLICACIÓN")
print("-------------------------------------------------------")

#Entrada
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

#Proceso
mult = num1 * num2

#Salida
print("La multiplicación entre ambos números es:", mult)

"""
-------------------------------------------------------
        EJERCICIO 5: CÁLCULO DE MULTIPLICACIÓN
-------------------------------------------------------
Ingrese un número: 7
Ingrese otro número: 14
La multiplicación entre ambos números es: 98
"""