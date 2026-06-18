"""
Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente
"""

try:
    edad=int(input("ingrese su edad: "))
    if edad > 0 and edad <120:
        print(f"su edad es: {edad}")
    else:
        print(f"{edad} no esta dentro de un rango esperado")
except ValueError:
    print("ah ingresado un tipo de dato erroneo")

