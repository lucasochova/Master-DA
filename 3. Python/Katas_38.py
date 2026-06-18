#!/usr/bin/env python
# coding: utf-8

# In[8]:


""" 
Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario
"""

def momento_dia(hora)->None:
    hora_format=int(hora.split(":")[0])

    if not 0 <= hora_format <= 23:
        raise ValueError(f"Hora inválida: {hora}. Debe estar entre 0 y 23.")

    if hora_format >=6 and hora_format <= 13:
        print(f"las {hora} horas, pertenecen a la mañana")
    elif hora_format >=13 and hora_format<=20:
        print(f"las {hora} horas, pertenecen a la tarde")
    else:
        print(f"las {hora} horas, pertenecen a la noche") 

get_hora=input("ingrese una hora en formato de 24hs. ")

momento_dia(get_hora)

