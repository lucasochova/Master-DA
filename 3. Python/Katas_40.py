#!/usr/bin/env python
# coding: utf-8

# In[9]:


""" 
Escribe una función que tome dos parámetros:  figura  (una cadena que puede ser  "rectangulo" ,  "circulo"  o 
"triangulo" ) y  datos  (una tupla con los datos necesarios para calcular el área de la figura)
"""

def calcular_figura(figura:str,datos:tuple)->float:
    figuras_validar=["rectangulo","circulo","triangulo"]
    if figura.lower() not in figuras_validar:
        raise ValueError("la figura no es valida")

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return 3.141592 * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

radio=(3,0)
baseyaltura=(2,3)
calcular_figura("circulo",radio)


# In[10]:


calcular_figura("triangulo",baseyaltura)


# In[11]:


calcular_figura("rectangulo",baseyaltura)

