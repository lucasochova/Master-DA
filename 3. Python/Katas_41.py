#!/usr/bin/env python
# coding: utf-8

# In[14]:


""" 
En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python.
"""
class salir(Exception):
    pass


def descuento(precio_origen:float)->float:
    try:
        valor_descuento=int(input("ingrese el valor del cupón: "))
        if valor_descuento<=0:
            print("el valor del cupon no puede ser 0")
            raise salir("No se pudo completar la operacion")
        nuevo_valor=precio_origen-valor_descuento
        if nuevo_valor<0:
            nuevo_valor=0
            return nuevo_valor
        return nuevo_valor
    except ValueError:
        print("debe ingresar un valor entero, numerico")
        raise salir("No se pudo completar la operacion")

try:
    original=float(input("ingrese el precio original de su articulo"))
    if original<=0:
        raise salir("el valor no puede ser 0")
    cupon=input("tiene un cupon de descuento? S/N: ")
    if cupon.lower()=="s":
        calculo=descuento(original)
        print(f"El total de su compra es {original}$, aplicando el descuento ud pagaria {calculo}$")
    elif cupon.lower()=="n":
        print(f"El total de su compra es de {original}$")
    else:
        raise TypeError()

except ValueError:
    print("debe ingresar un valor numerico")

except TypeError:
    print("Debe ingresar S o N")

except salir as s:
    print(s)

finally:
    print("Que tenga un buen dia")

