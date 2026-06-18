#!/usr/bin/env python
# coding: utf-8

# In[5]:


""" Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""

def diferencia(lista1: list, lista2:list) -> list: # generamos la funcion, pedimos dos listas
    lista_salida=list(map(lambda x,y: x - y, lista1, lista2))
    """ list convierte el resutado de map (objeto) en lista, map recorre las listas
        item por item, lambda recoge el "item" que le indica map, de ambas listas
        los transforma en X e Y y ejecuta la funcion " - " diferencia"""
    return lista_salida

lista_A=[10,20,30,40]
lista_B=[5,5,5,5]
calculo = diferencia(lista_A,lista_B)
calculo


# In[ ]:


#Version mejorada
def diferencia(lista1: list, lista2:list) -> list: # generamos la funcion, pedimos dos listas
    if len(lista1) != len(lista2) #verifica si las listas tienen la misma longitud
        print("las listas tienen diferente longitud")
    else
        lista_salida=list(map(lambda x,y: x - y, lista1, lista2))
    """ list convierte el resutado de map (objeto) en lista, map recorre las listas
        item por item, lambda recoge el "item" que le indica map, de ambas listas
        los transforma en X e Y y ejecuta la funcion " - " diferencia"""
    return lista_salida

