"""
Desarrolle un algoritmo que permita al usuario elegir un valor entero, y que de un arreglo
desordenado elimine todos los valores que se repitan del mismo. Una vez eliminados todos los
valores deberá informar cuantas eliminaciones hizo, por ejemplo: “Se han eliminado 8 veces el
mismo valor”. Por ultimo deberá preguntar al usuario si desea eliminar otro valor o no.
"""

import random

#declaramos 
valores = []
opcion = str()
contador = 0

#asignamos valores random al array
for i in range(20):
    valor = random.randint(0,10)
    valores.append(valor)

#imprimimos el array
print(valores)

#creamos un while para que se vuelva a ejecutar hasta que no quieran eliminar más valores
while opcion.lower() != "n":
    #pedimos ingresar un valor a eliminar
    valor_eliminado = int(input("Ingrese un valor entero a eliminar: "))

    #recorremos la lista
    for f in valores:
        #si el valor se encuentra en la lista...
        if valor_eliminado in valores:
            #borramos el valor
            valores.remove(valor_eliminado)
            #sumamos un valor al contador
            contador = contador + 1

    #imprimimos por pantalla el valor a eliminar y la cantidad de veces eliminado
    print(f"El valor {valor_eliminado} se ha eliminado {contador} veces.")
    
    #preguntamos si se desea eliminar otro valor o no
    opcion = str(input("¿Desea eliminar otro valor? s/n: "))

print("- Fin del programa -")