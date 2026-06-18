#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 
corresponde al número quinientos setenta y dos 572. Usa la función  reduce()
"""
#importamos la funcion reduce()
from functools import reduce
#definimos nuestras funcion, pedimo la lista de numeros
def unir(numeros:list)->int:
    #reduce iterara en la lista de numeros, los valores se iran sumando y 
    #desplazando uno a uno conformando el numero final: i sera el iterador, acumulador una variable
    #temporal que nos permitira desplazar el numero anterior
    union=reduce(lambda acumulador,i:acumulador*10+i,numeros)
    #retornamos el valor concatenado
    return union

lista=[1,2,3,4,5,6]
total= unir(lista)
total

