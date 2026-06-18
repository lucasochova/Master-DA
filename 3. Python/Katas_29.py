#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro.
"""

def enmascarar(frase)->str:
    #convierte la variable en string
    cadena=str(frase)
    #si el string tiene menos de 4 caracteres, devuelve el string sin procesar
    if len(cadena) <= 4:
        return cadena
    #si el string tiene mas de 4 caracteres, generamos "#" por el largo total menos 4 de la 
    #cadena y agregamos los ultimos 4 digitos del string original
    return '#' * (len(cadena) - 4) + cadena[-4:]

referencia=1567865243846
mask=enmascarar(referencia)
mask

