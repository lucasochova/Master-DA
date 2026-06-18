#!/usr/bin/env python
# coding: utf-8

# In[9]:


# """ 
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
# lanza una excepción.
# """

nombres_concat=input("ingrese una lista de nombres, separados por comas: ")
nombres_list=nombres_concat.split(", ")
nombres_list
buscar=input("ingrese un nombre para buscar en el sistema: ")
if buscar in nombres_list:
    print(f"se ha encontrado a '{buscar}' en el sistema")
else:
    print("no hubo conincidencias en la busqueda")

