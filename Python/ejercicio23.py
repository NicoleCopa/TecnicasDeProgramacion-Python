"""
Las notas del 1er parcial de los alumnos de un curso se encuentran cargadas en un arreglo
unidimensional de 100 componentes. Actualmente se han cargado 63 notas en total. Teniendo
en cuenta que la materia es promocional, y que promocionan todos aquellos que han obtenido
un puntaje igual o mayor a 7(siete) confeccione un algoritmo que:
a) Que informe la cantidad de alumnos que han promocionado la materia.
b) Que informe la cantidad de alumnos que hayan aprobado sin promocionar.
c) Que informe la cantidad de alumnos que no han aprobado la materia.
d) Al finalizar el programa debe preguntar al usuario si necesita cargar una nota para (en caso de que se hay olvidado alguna)
(utilice la función AZAR para cargar las notas que varían entre 1 y 10)
"""

import random

notas = [None] * 100

# Cargar las notas existentes
for i in range(63):
    notas[i] = random.randint(1, 10)

# Contadores para las diferentes categorías
promocionados = 0
aprobados = 0
desaprobados = 0

# Verificar las notas y actualizar los contadores
for nota in notas:
    if nota is not None:
        if nota >= 7:
            promocionados += 1
        elif nota >= 4:
            aprobados += 1
        else:
            desaprobados += 1

# Mostrar los resultados
print("Cantidad de alumnos que han promocionado la materia:", promocionados)
print("Cantidad de alumnos que han aprobado sin promocionar:", aprobados)
print("Cantidad de alumnos que no han aprobado la materia:", desaprobados)

# Preguntar si se necesita cargar más notas
opcion = input("¿Necesita cargar una nota adicional? (s/n): ")
if opcion.lower() == "s":
    nota_adicional = random.randint(1, 10)
    notas.append(nota_adicional)
    print("Se ha cargado la nota", nota_adicional)
    
print("Fin del programa.")