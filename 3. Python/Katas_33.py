#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Crea una función  lambda  que sume elementos correspondientes de dos listas dadas
"""
# Lista 1: Nombres de empleados
nombres = [
    "Ana García",
    "Carlos López",
    "María Martínez",
    "Luis Sánchez",
    "Sofía Ramírez",
    "Jorge Herrera",
]

# Lista 2: Puestos de empleados
puestos = [
    "Desarrolladora Senior",
    "Gerente de Proyectos",
    "Diseñadora UX",
    "Analista de Datos",
    "DevOps Engineer",
    "QA Tester",
]

#el siguiente lambda no contempla si alguna de las listas tuviese mas o menos items que la otra
#y solo sumar elementos de un mismo tipo
suma=list(map(lambda x,y:x+y, nombres, puestos))
suma


# In[ ]:




