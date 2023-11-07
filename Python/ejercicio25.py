"""
Desarrolle un algoritmo que permita al usuario elegir un valor entero, y que de un arreglo
desordenado elimine todos los valores que se repitan del mismo. Una vez eliminados todos los
valores deberá informar cuantas eliminaciones hizo, por ejemplo: “Se han eliminado 8 veces el
mismo valor”. Por ultimo deberá preguntar al usuario si desea eliminar otro valor o no.
"""

import random

valores = []

for i in range(100):
    valor = random.randint(0,50)
    valores.append(valor)

