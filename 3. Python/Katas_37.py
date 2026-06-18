#!/usr/bin/env python
# coding: utf-8

# In[19]:


""" 
Crea una función llamada  procesar_texto  que procesa un texto según la opción especificada:  contar_palabras , 
reemplazar_palabras ,  eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro 
de la función  procesar_texto .
Código a seguir:
    Crear una función  contar_palabras  para contar el número de veces que aparece cada palabra en el texto. Tiene 
    que devolver un diccionario.
    Crear una función  reemplazar_palabras  para remplazar una  palabra_original  del texto por una  palabra_nueva . Tiene 
    que devolver el texto con el remplazo de palabras.
    Crear una función  eliminar_palabra  para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
    Crear la función  procesar_texto  que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
    número de argumentos variable según la opción indicada.
Caso de uso:
    Comprueba el funcionamiento completo de la función  procesar_texto
"""

def contar(cadena: str) -> dict:
    """
    Recibe una cadena de texto y devuelve un diccionario
    con la frecuencia de cada palabra.
    """
    palabras_cadena= cadena.lower().split()
    frecuencias = {} #crea diccionario
    for palabra in palabras_cadena:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    print(frecuencias)
    return frecuencias

def reemplazar(cadena: str, palabra: str, nueva: str) -> str:
    procesado = cadena.lower().split()
    reemplazado = " ".join(map(lambda x: nueva if x == palabra else x, procesado))
    return reemplazado

def eliminar(cadena:str, e_palabra:str)->str:
    procesado=cadena.lower().split()
    nueva_cadena =" ".join(map(lambda x: "" if x == e_palabra else x, procesado))
    return nueva_cadena

def procesar_texto(texto:str ,opcion:str ,palabra_busqueda:str = "",palabra_remplazo:str="")->str:
    if opcion.lower()=="contar":
        contar(texto)
        return

    if opcion.lower()=="reemplazar":
        return reemplazar(texto, palabra_busqueda,palabra_remplazo)

    if opcion.lower()=="eliminar":
        return eliminar(texto, palabra_busqueda)

    print("debe seleccionar una opcion valida")

referencia = "sol luna luna mar mar mar casa casa casa casa río río río río río cielo cielo cielo cielo cielo cielo"
procesar_texto(referencia,"contar")


# In[16]:


nuevo=procesar_texto(referencia,"reemplazar","casa","tienda")
nuevo


# In[21]:


borrar=procesar_texto(referencia,"eliminar","cielo")
borrar

