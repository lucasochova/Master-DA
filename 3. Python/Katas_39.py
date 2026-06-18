#!/usr/bin/env python
# coding: utf-8

# In[14]:


""" 
Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
Las reglas de calificación son:
    0  69 insuficiente
    70 79 bien
    80 89 muy bien
    90 100 excelente
"""

def calificar(nota:int)->str:
    if not -1 < nota <101:
        raise ValueError("El valor no esta en un rango aceptable")
    if nota <= 69:
        print(f"insuficiente")
        return "insuficiente"
    if 70 <= nota <= 79:
        print("bien")
        return "bien"
    if 80 <= nota <= 89:
        print("muy bien")
        return "muy bien"
    if nota >= 90:
        print("excelente")
        return "excelente"

calificar(100)

