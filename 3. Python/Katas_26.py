#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Crea una función  lambda  que calcule el resto de la división entre dos números dados.
"""
#esta funcion no tiene proteccion contra errores, se puede introducir un valor 0 en el divisor
#ZeroDivisionError no esta contemplada
resto = lambda x,y: x%y

numero_a=2
numero_b=4

calculo=resto(numero_a,numero_b)
calculo

