#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Genera una función que al recibir una frase devuelva
una lista con la longitud de cada palabra. Usa la función  map()
"""

def largo(frase:str)->list:
    analisis=frase.split()
    palabras=list(map(lambda palabra:(palabra,len(palabra)),analisis))

    return palabras


frase = "una frase con palabras variadas"

largo_palabras=largo(frase)
largo_palabras

