#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""

ingreso = input("ingrese una serie de numeros") #ingreso una lista de numeros (suceptible a fallos)
lista=[] #defino mi lista vacia
for numeros in ingreso: #itero entre los caracteres
    lista.append(int(numeros)) #convierto los caracteres en enteros y los agrego a mi lista

print(lista) #verificacion


# In[11]:


doble = list(map(lambda x: x*2,lista)) 
""" 
    utilizando map, itero dentro de la lista y lambda ejecuta la operacion, como map regresa un objeto
    lo convertimos a lista nuevamente con list
"""
print(doble)

