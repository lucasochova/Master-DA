#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función  map()
"""
#se utlizo la guia de cluadecode y llama3.1 para comprender y utilizar dict.fromkeys
def mayus_minus(conjunto:str)->list:
    #creamos un diccionario con nuestro string, eliminamos los espacios y eliminamos los repetidos
    diccionario=dict.fromkeys(letra.upper() for letra in conjunto if letra.isalpha())
    #recorremos el diccionario letra por letra y a partir de ellas, creamos una tupla con su mayus y minus
    #convertimos nuestra lista de tuplas en una lista y devolvemos la funcion
    lista_may_min=list(map(lambda l:(l.upper(),l.lower()),diccionario))
    return lista_may_min

palabra="una frase para analizar"
letras=mayus_minus(palabra)
letras

