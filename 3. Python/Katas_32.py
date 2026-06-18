#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" 
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.
"""

empleados = [
    {"nombre": "Ana García",    "puesto": "Desarrolladora Senior"},
    {"nombre": "Carlos López",  "puesto": "Gerente de Proyectos"},
    {"nombre": "María Martínez","puesto": "Diseñadora UX"},
    {"nombre": "Luis Sánchez",  "puesto": "Analista de Datos"},
]

nombre="carlos lópez"

def buscar_empleado(lista_empleados:list[dict],buscar:str)->str:
    for empleado in lista_empleados:
        if empleado["nombre"].lower()==buscar.lower():
            return empleado["puesto"]
    return "la persona no trabaja aqui"

busqueda=buscar_empleado(empleados,nombre)
busqueda

