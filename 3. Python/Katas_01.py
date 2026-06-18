#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
01 -Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados.
"""

def frecuencia_letras(cadena: str) -> dict:
    """
    Recibe una cadena de texto y devuelve un diccionario
    con la frecuencia de cada letra.
    """
    frecuencias = {} #crea diccionario
    for letra in cadena:
        if letra != ' ': #ignora espacios
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

texto = input("ingrese un texto para analizar") #ingresa la cadena de caracteres
resultado = frecuencia_letras(texto) #procesa la cadena
print(resultado) #imprime el resultado


