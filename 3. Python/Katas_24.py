#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" 
Calcula la diferencia total en los valores de una lista. Usa la función  reduce()
"""
from functools import reduce

def diferencia(numeros:list)->int:
    calculo=reduce(lambda buffer,valor:buffer-valor,numeros)
    return calculo

lista_n=[1,2,3,4,5,6,7,8]
total=diferencia(lista_n)
total

