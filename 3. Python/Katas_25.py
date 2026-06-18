#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" 
Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

cadena="esto es una cadena de prueba"

def contar_c(cadena:str)->int:
    return len(cadena)

largo=contar_c(cadena)
largo

