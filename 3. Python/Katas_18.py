#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
90. Usa la función  filter()
"""

estudiantes = [
    {'nombre': 'Juan', 'edad': 20, 'calificacion': 85},
    {'nombre': 'Maria', 'edad': 22, 'calificacion': 92},
    {'nombre': 'Pedro', 'edad': 21, 'calificacion': 78},
    {'nombre': 'Ana', 'edad': 19, 'calificacion': 95},
    {'nombre': 'Carlos', 'edad': 23, 'calificacion': 88}
]
#pedimos la lista de diccionarios
def destacados(alumnos:list)->list:
    #con fiter iteramos por la lista y con lambda preguntamos por la clave calificacion del diccionario 
    #si su valor es mayor o igual a 90 en este caso, guardamos el diccionario en una nueva lista
    #y lo regresamos a la funcion principal.
    resultado=list(filter(lambda x: x['calificacion']>=90 ,alumnos))
    return resultado

aprobados_90=destacados(estudiantes)
aprobados_90

