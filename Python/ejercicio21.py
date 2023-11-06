"""
Desarrolle un algoritmo que permita calcular el promedio de las notas que tiene un alumno en
la materia Técnicas de Programación, teniendo en cuenta que son 2 calificaciones numéricas (2
parciales) y una calificación valorativa tipo “APROBO-NO APROBO” (trabajo practico)

a) El programa debe permitir que el usuario ingrese la cantidad de alumnos de la materia que
tienen las 3 notas. (ej. 50 alumnos)

b) El programa debe permitir al usuario cargar las tres notas y posteriormente mostrar el
promedio del alumno por pantalla.

c) Una vez obtenido el promedio informar si el alumno PROMOCIONO la materia o si APROBO LA CURSADA.

d) Tener en cuenta que, para esto último, el TP de la materia debe estar APROBADO, si el TP
está NO APROBADO deberá informar que el alumno NO APROBO la cursada.

NOTA: las condiciones para la promoción, aprobación o no aprobación de la cursada son las
misma que rigen en nuestra materia salvo las particularidades de combinaciones de notas para
la promoción. PS - DF

PROMOCION = 7-10 - APROBO
ARPOBADO = 4-6 - APROBO
NO APRO0BACION = 0 - 3 NO APROBO 
"""

contador = int()
alumnos = int()
nota1 = int()
nota2 = int()
nota3 = int()
promedio = float()

alumnos = int(print("Ingrese la cantidad de alumnos de la materia que tienen las 3 notas: "))

while contador <= alumnos:
    nota1 = int(input("Ingrese la primera nota 1-10: "))
    nota2 = int(input("Ingrese la segunda nota 1-10: "))
    nota3 = int(input("Ingrese la tercera nota 1- APROBÓ / 2- NO APROBÓ: "))
    promedio = nota1+nota2/2
    print(promedio)
    if promedio >= 7 and nota3 == 1:
        print("El alumno PROMOCIONÓ la materia")