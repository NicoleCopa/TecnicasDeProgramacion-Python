"""
En un arreglo de 20 componentes se encuentran cargados los nombres de 17 invitados, cada
nombre es diferente.
a) Agregue a la lista los nombres de 3 invitados que faltan para completar la misma (operación de Inserción).
b) En la lista hay un nombre que no estaba invitado, cargue por pantalla ese nombre y elimínelo de la lista.
"""

invitados = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Sofía", "Miguel", "Lucía", "Diego", "Valentina", "Andrés", "Camila", "José", "Isabella", "Gabriel"]

for i in range(3):
    nombre = str(input("Ingrese el nombre del invitado faltante: "))
    invitados.append(nombre)
    
print("Los invitados son:")
print(invitados)

no_invitado = str(input("Ingrese el nombre del que no estaba invitado: "))

if no_invitado in invitados:
    invitados.remove(no_invitado)
    print(f"{no_invitado} no estaba invitado y fue aliminado de la lista.")
else:
    print(f"{no_invitado} no estaba en la lista de invitados.")

print(invitados)