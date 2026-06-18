#!/usr/bin/env python
# coding: utf-8

# In[3]:


""" 
Concatena una lista de palabras.Usa la función  reduce()
"""

from functools import reduce

lista_palabras=['hola','mundo','esto','era','una','lista']

def concatenar(lista:list)->str:
    resultado=str(reduce(lambda buffer,palabra: buffer + ' ' + palabra,lista))
    return resultado

union=concatenar(lista_palabras)
union

