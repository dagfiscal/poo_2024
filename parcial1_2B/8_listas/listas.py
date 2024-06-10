"""

 List (Array)
 son coleciones o conjunto de datos/valores bajo 
 un mismo nombre, para acceder a los valores se
 hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

#Ejemplo 1 crear una lista de numeros e imprimir el contenido

# numeros=[23,34]
# print(numeros)

# #Recorrer la lista con ciclo for
# for i in numeros:
#     print(i)

# #Recorrer la lista con ciclo while

# i=0
# while i<=len(numeros)-1:
#     print(numeros[i])
#     i+=1    


#Ejemplo 2 crear una lista de palabras y posteriormete buscar  la coincidencia de una palabra 

# import os

# os.system("clear")

# palabras=["naranja","utd","america","naranja"]
# print(palabras)

# palabra_buscar=input("Ingresa la palabra a buscar: ")

# encontro=False

# for i in palabras:
#   if i==palabra_buscar:
#     print(f"Se encontra la palabra {palabra_buscar} en la posicion {palabras.index(i)}")
#     encontro=True

# i=0
# while i<len(palabras):
#   if palabras[i]==palabra_buscar:
#     print(f"Se encontra la palabra {palabra_buscar} en la posicion {i}")
#     encontro=True 
#   i+=1    
    
# if not encontro:
#   print("No se encontro la palabra a buscar")  


#Ejemplo 3 Agregar y Eliminar elementos de una lista
# os.system("clear")

# numeros=[23,34,23]
# print(numeros)

# #agregar un elemento
# numeros.append(100) 
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

# #eliminar un elemento
# numeros.remove(100) #indicar el elemento a borrar
# print(numeros)
# numeros.pop(2) #indicar la posicion del el elemento a borrar
# print(numeros)

#Ejemplo 4 crear una lista multilinea (matriz) para agregar los nombres y numeros telefonicos

# agenda=[
#   ["Carlos",6181234567],
#   ["Leo",6671234576],
#   ["Sebastian",6182341234],
#   ["Pedro",6171236789]
# ]

# print(agenda)

# for i in agenda:
#   print(f"{agenda.index(i)+1}.-{i}")

#ejemplo 5 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas. 
#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas  

import os

def insertarPeliculas():
    pelicula=input("Ingresa el nombre de la pelicula: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPeliculas():
    pelicula=input("Ingresa el nombre de la pelicula: ")
    peliculas.remove(pelicula)
    espereTecla()    


peliculas=[]

print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- SALIR ")
opcion=input("\t Elige una opción: ").upper()

if opcion=="1" or opcion=="AGREGAR":
    insertarPeliculas()
elif opcion=="2" or opcion=="REMOVER":
    eliminarPeliculas() 

