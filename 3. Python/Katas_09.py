#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función  filter()
"""
#creamos las listas de referencia
lista_no_permitidos=["Mapache","Tigre","Serpiente Pitón","Cocodrilo","Oso"]
animales = ["Perro","Gato","Conejo","Loro","Hámster","Pez","Erizo","Mapache","Tigre","Oso"]

    """con la funcion filter, iteramos la lista objetivo, y preguntamos con lambda y not in a la lista de referencia
    sin el item esta o no en la misma, si el item esta en la lista, devuelve un false, por lo que lo quitamos de la lista de salida
    el resultado de la iteracion sera un objeto filter, el cual convertiremos a lista, para luego guardarlo en una variable.
    """
animales_permitidos=list(filter(lambda animales: animales not in lista_no_permitidos,animales))
animales_permitidos

