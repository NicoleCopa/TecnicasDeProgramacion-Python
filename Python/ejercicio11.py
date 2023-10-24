"""Escribir un programa que calcule el área de un círculo, dado su radio. 
El usuario debe ingresar el valor del radio. """

import math

radio = float(input("Ingrese el radio del círuclo: "))

area = math.pi * (radio**2)

print(f"El área del círulo es: {area:.2f}")
