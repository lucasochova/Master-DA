#!/usr/bin/env python
# coding: utf-8

# In[5]:


""" 
Crea una función que calcule el promedio de una lista de números.
"""

def promedio(numeros:list)->int:

    return sum(numeros)/len(numeros)

lista=[1,2,3,4,5,6,7,8,9]
calculo=promedio(lista)
calculo

