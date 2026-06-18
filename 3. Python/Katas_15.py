#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" 
Crea una función  lambda  que  sume 3 a cada número de una lista dada
"""

lista=[1,2,3,4,5,6]

lista_mas3 = list(map(lambda x: x+3,lista))
lista_mas3

