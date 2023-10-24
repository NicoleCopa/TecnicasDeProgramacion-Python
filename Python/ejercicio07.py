"""Escribir un programa que calcule la distancia entre dos puntos en un plano cartesiano,
dados sus coordenadas. El usuario debe ingresar las coordenadas de ambos puntos. 
Tenga en cuenta el siguiente grafico para la resolución."""

import math

print("""-------------------------------------------------------)
                EJERCICIO 7: COORDENADAS
-------------------------------------------------------""")

x1 = float(input("Ingrese la coordenada X1: "))
x2 = float(input("Ingrese la coordenada X2: "))
y1 = float(input("Ingrese la coordenada Y1: "))
y2 = float(input("Ingrese la coordenada Y2: "))

coordenada = math.sqrt( ((x2-x1)**2) + ((y2 - y1)**2))
                       
print(f"La coordenada del plano cartesiano es: {coordenada}")

"""
-------------------------------------------------------
                EJERCICIO 7: COORDENADAS
-------------------------------------------------------
Ingrese la coordenada X1: 3
Ingrese la coordenada X2: 6
Ingrese la coordenada Y1: 2
Ingrese la coordenada Y2: 8
La coordenada del plano cartesiano es: 6.708203932499369
"""