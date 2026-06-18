#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
    Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
    excepción personalizada y maneja el error adecuadamente.
"""
def promedio(lista:list)->int:
    if len(lista)!=0:
        prom=sum(lista)/len(lista)
    else:
        print("debe ingresar al menos un valor.")

    return prom

numeros=[1,2,3,4,5,6]
calculo=promedio(numeros)
calculo

