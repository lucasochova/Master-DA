#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" 
Crea una función  lambda  que filtre los números impares de una lista dada
"""
lista=[1,2,3,4,5,6,7,8,9,10]
filtrado=list(filter(lambda x: x%2==0,lista))
filtrado

