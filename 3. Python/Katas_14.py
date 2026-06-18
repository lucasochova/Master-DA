#!/usr/bin/env python
# coding: utf-8

# In[4]:


""" 
Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.
Usa la función  filter()
"""

def filtrar_inicio(lista:list,letras:str)->list:
    filtrado=list(filter(lambda c:letras in c, lista))
    return filtrado


palabras=["hola","hombre","haber","perro"]
letra="h"
resultado=filtrar_inicio(palabras,letra)
resultado

