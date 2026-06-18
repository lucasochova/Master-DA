#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
    Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado
"""
#creamos nuestras variables
notas = [6,7,8,6]
nota_aprobado = 5

#definimos nuestras funcion que pedira la lista y el umbral para definir el aprobado
def evaluar(lista: list,umbral:int)-> tuple:
    #calculamos el promedio, sumando y dividiendo por la cantidad de items sumados
    promedio=0
    for valor in lista: promedio += valor
    promedio = promedio/len(lista)

    #creamos la respuesta dependiendo de la nota umbral
    if promedio> umbral:
        aprobado="aprobado"
    else:
        aprobado="desaprobado"

    #regresamos el valor y su evaluacion
    resultado={promedio,aprobado}
    return resultado

alumno=evaluar(notas,nota_aprobado)
alumno

