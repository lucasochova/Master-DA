#!/usr/bin/env python
# coding: utf-8

# In[5]:


""" 
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.
"""

def anagrama(palabra1:str ,palabra2:str)->str:
    if sorted(palabra1)!=sorted(palabra2):
        return print("las palabras no son anagramas")
    else:
        return print("las palabras son anagramas")        

p1="hola"
p2="aloh"

anagrama(p1,p2)

