#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función  map()"""
#definimos nuestra lista
lista=[
    ('elemento', 1),
    ('elemento', 2),
    ('elemento', 3),
    ('elemento', 4)
]
#la funciona itera a travez de la lista, convirtiendo una a una las tuplas en strings
lista2=list(map(lambda x: str(x), lista))
lista2

