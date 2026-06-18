#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo"""

lista_palabras=["gato", "perro", "árbol", "río", "sombra", "sol"]
palabra_busqueda="ol"

def encontrar_palabras(lista_base: list, palabra: str) -> list: #definimos la funcion 
    nueva_lista = [] #definimos nuestra nueva lista
    for items in lista_base: #iteramos la cantidad de palabras que hayamos enviado
        if palabra.lower() in items.lower(): #preguntamos si nuestra palabra objetivo esta contenida en la palabra de la lista
            nueva_lista.append(items) #guardamos la palabra
    return nueva_lista #devolvemos la lista de coincidencias

encontrado=encontrar_palabras(lista_palabras,palabra_busqueda) #ejecutamos la funcion
print(encontrado)

