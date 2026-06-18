#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
    Escribe una función que calcule el factorial de un número de manera recursiva.
"""
#definimos el numero que queremos calcular
numero=6

def factorial(num:int)-> int:
    calculo =1 #creamos una variable para operar
    while num>1:
        calculo=calculo*num
        num-=1
        #multiplicamos todos los valores para calcular el factorial
    return calculo

calcular=factorial(numero)
calcular

