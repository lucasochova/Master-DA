#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada
"""

def duplicados(lista:list)->str:
    #creamos una lista (set) de datos vacio, que nos permirita almacenar nuestros datos para el analisis
    vistos = set()
    for elemento in lista:
        #iteramos uno a uno los datos
        if elemento in vistos:
            #si el dato se encuentra en nuestro conjunto temporal, devolvemos el dato duplicado
            return elemento
        #si el dato no esta en el conjunto temporal, lo agregamos y seguimos iterando
        vistos.add(elemento)
    #si la iteracion llega al final y no hubo duplicados, devolvemos none
    return None    

lista_d=['hola','mundo','elemento','mundo','hola']
analizar=duplicados(lista_d)
analizar

