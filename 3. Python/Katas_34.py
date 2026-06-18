#!/usr/bin/env python
# coding: utf-8

# In[11]:


""" 
Crea la clase  Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco ,  nueva_rama ,  crecer_ramas ,  quitar_rama  e  info_arbol . El objetivo es implementar estos métodos para 
manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método  crecer_tronco  para aumentar la longitud del tronco en una unidad.
3. Implementar el método  nueva_rama  para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método  crecer_ramas  para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método  quitar_rama  para eliminar una rama en una posición específica.
6. Implementar el método 
info_arbol  para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
mismas.
"""

class Arbol:
    def __init__(self,nombre="Grout"):
        self.nombre=nombre
        self.tronco=1
        self.ramas=[]
        print(f"{self.nombre} ha nacido")
        pass

    def crecer_tromco(self):
        self.tronco+=1
        print(f"{self.nombre} ha desarrolado su tronco.")

    def nueva_rama(self):
        if len(self.ramas)==0:
            self.ramas=[1]
            print(f"{self.nombre} tiene su primer rama")
        else:
            self.ramas.append(1)
            print(f"{self.nombre} tiene una nueva rama con un total de {len(self.ramas)}")

    def crecer_rama(self):
        for rama in range(len(self.ramas)):
            self.ramas[rama]+=1
        print("todas las ramas han crecido")

    def eliminar_rama(self,posicion:int):
        largo=self.ramas.pop(posicion-1)
        print(f"se ha eliminado la {posicion}º ramas y tenia un largo de {largo}")


    def info_arbol(self):
        print(f"su arbol {self.nombre} tiene una altura de {self.tronco}, tiene {len(self.ramas)} ramas, sus ramas tienen la siguiente longitud")
        for rama in range(len(self.ramas)):
            print(f"rama{rama+1}: {self.ramas[rama]}")

brote=Arbol("pepe")


# In[2]:


brote.crecer_tromco()


# In[7]:


brote.nueva_rama()


# In[8]:


brote.crecer_rama()


# In[9]:


brote.info_arbol()


# In[10]:


brote.eliminar_rama(2)

