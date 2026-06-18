#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
todas las palabras que sean más largas que n. Usa la función  filter()
"""
#definimos la funcion, pedimos un string y un entero
def largo_mayor(texto:str ,Largo:int)->list:
    #separamos el string en palabras y lo guardamos como una lista
    analisis=texto.split()
    #procesamos una palabra a la vez y si lambda nos regresa verdadero, guardamos la palabra en nuestra nueva variable
    mayores=list(filter(lambda x: len(x)>largo,analisis))
    #regresamos la nueva lista
    return mayores


cadena="hola esto es una prueba de longitud de texto"
largo=3
palabras=largo_mayor(cadena,largo)
palabras

