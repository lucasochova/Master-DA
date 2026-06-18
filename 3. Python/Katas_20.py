#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" 
Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
filter()
"""

lista=[1,2,3,4,'a','b','c','d']

def separar_enteros(listamix:list)->list:

    lista_enteros=list(filter(lambda t: type(t)==int ,listamix))
    return lista_enteros

procesado=separar_enteros(lista)
procesado

