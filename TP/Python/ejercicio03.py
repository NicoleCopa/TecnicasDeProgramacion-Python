"""
Escribir un algoritmo que permita al usuario calcular una potencia y luego muestre el 
resultado de este cálculo. Para ello el usuario debe ingresar un número y luego su exponente.
Es decir. Ejemplo: 5**2 = 25 (5 elevado al cuadrado, es igual a 25) 
_______________________________________
ENTRADA                 IDENTIFICADOR
    Numero                  num
    Exponente               exp
SALIDA
    Potencia                pot
_______________________________________
"""

#Decoracion: Nombre del algorítmo
print("-------------------------------------------------------")
print("         EJERCICIO 3: CÁLCULO DE POTENCIA")
print("-------------------------------------------------------")

#Entrada
num = int(input("Ingrese un número: "))
exp = int(input("Ingrese su exponente: "))

#Proceso
pot = num**exp

#Salida
print("La potencia del número es:", pot)

"""
-------------------------------------------------------
           EJERCICIO 3: CÁLCULO DE POTENCIA
-------------------------------------------------------
Ingrese un número: 5
Ingrese su exponente: 2
La potencia del número es: 25
"""