#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no
"""
#creamos un bucle infinito que nos permita probar todas las posibilidades
salida=True
while salida: 
    try:#ingresamos los valores, al convertir a float, podemos saber si el valor ingresado es numerico
        val1=float(input("Ingrese un valor numerico para ser dividido: "))

        val2=float(input("ingrese in valor numerico mayor a 0 para dividir: "))
        #realizamos la division
        resultado=val1/val2

    except ValueError: #si los valores no son numericos nos muestras el siguiente texto
        print("debe ingresar valores numericos")

    except ZeroDivisionError: #si el segundo valor es 0 nos mostrara el siguiente texto
        print("debe ingresar un valor diferente a 0 para dividir")

    else: #si todo el codigo se ejecuto sin problema, nos enseñara el resultado y nos dejara salir del bucle
        print(f"dvision exitosa: {val1}/{val2} es igual a: {resultado}")
        salida = False
        print("programa finalizado")

