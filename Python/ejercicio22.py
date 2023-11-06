""" Desarrolle un algoritmo para cargar con valores enteros un arreglo de 50 componentes
utilizando la función AZAR. El usuario le debe indicar al programa cuantos valores cargar y el
rango de valores (por ejemplo, si es de 0 a 100, debe ingresar por pantalla el valor 100). Al
finalizar deberá informar si el arreglo está completo o no. Por ultimo si el arreglo no está
completo deberá preguntar al usuario si desea seguir cargando valores o no. PS - DF """

import random

arreglo = []

while len(arreglo) < 50:
    
    cantidad = int(input("Ingrese la cantidad de valores a cargar: "))
    rango = int(input("Ingrese el rango de valores (ej: si es de 0 a 100, ingrese 100): "))
    
    #agregamos x cantidad de valores de x rango
    for i in range(cantidad):
        #sacamos valor random
        valor = random.randint(0, rango)
        #agregamos valor al array
        arreglo.append(valor)

        #si la cantidad del array es = 50...
        if len(arreglo) == 50:
            break #terminamos
    
    #si el array es menor a 50...
    if len(arreglo) < 50:
        opcion = str(input("El array está incompleto. ¿Desea ingresar más? s/n: "))
        #si opcion es NO, entonces termina la ejecución
        if opcion.lower() == "n":
            break
    
print("\nEl array conteiene los siguientes valores:")
print(arreglo)
    
if len(arreglo) == 50:
    print("El array está completo.")
else:
    print("El array está incompleto.")
