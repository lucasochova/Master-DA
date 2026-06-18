#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" 
Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función  reduce()
"""
from functools import reduce
lista_numeros=[1,2,3,4,5]

producto=reduce(lambda x,y:x*y,lista_numeros)
producto

