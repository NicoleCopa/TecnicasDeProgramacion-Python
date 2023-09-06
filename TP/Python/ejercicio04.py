"""
Escribir un algoritmo que permita al usuario ingresar dos números 
(el 1er número es el radicando, y el 2do número es el índice) para calcular la raíz y 
uego le muestre al usuario el resultado de este cálculo. 
Ejemplo: √25 = 5 (raíz cuadrada de 25, es igual a 5, se deberá permitir al usuario 
ingresar el 25 y el 2 que actuará de indice)
_______________________________________
ENTRADA                 IDENTIFICADOR
    Numero                  num
    Exponente               exp
SALIDA
    Potencia                pot
_______________________________________
"""
#importamos libreria
import math

#Decoracion: Nombre del algorítmo
print("-------------------------------------------------------")
print("         EJERCICIO 3: CÁLCULO DE RAÍZ")
print("-------------------------------------------------------")

#Entrada
rad = int(input("Ingrese el radicando: "))
ind = int(input("Ingrese el índice: "))

#Proceso
raiz = rad ** (1/ind)

#Salida
print("La raíz es:", raiz)

"""
-------------------------------------------------------
           EJERCICIO 3: CÁLCULO DE POTENCIA
-------------------------------------------------------
Ingrese un número: 5
Ingrese su exponente: 2
La potencia del número es: 25
"""