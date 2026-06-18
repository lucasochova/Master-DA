#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Crea la clase  UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
corriente. 
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
agregar dinero al saldo.
Código a seguir:
    Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante  True  y  False .
    Implementar el método  retirar_dinero  para retirar dinero del saldo del usuario. 
        Lanzará un error en caso de no poder hacerse.
    Implementar el método  transferir_dinero  para realizar una transferencia desde otro usuario al usuario actual. 
        Lanzará un error en caso de no poder hacerse.
    Implementar el método  agregar_dinero  para agregar dinero al saldo del usuario.
Caso de uso:
    Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    Agregar 20 unidades de saldo de "Bob".
    Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    Retirar 50 unidades de saldo a "Alicia"
"""
class UsuarioBanco:
    def __init__(self, nombre: str, saldo: int = 0, cuenta_corriente: bool = False) -> None:
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
        print(f"Su cuenta ha sido creada, {self.nombre}. Su saldo es: {self.saldo}")

    def retirar_dinero(self, monto_retiro: int) -> None:
        if monto_retiro > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        self.saldo -= monto_retiro
        print(f"{self.nombre} retiró {monto_retiro}. Saldo actual: {self.saldo}")

    def agregar_dinero(self, monto_ingreso: int) -> None:
        self.saldo += monto_ingreso
        print(f"{self.nombre} agregó {monto_ingreso}. Saldo actual: {self.saldo}")

    def transferir(self, usuario: "UsuarioBanco", monto: int) -> None:
        if monto > usuario.saldo:
            print(f"Saldo insuficiente en la cuenta de {usuario.nombre}.")
        else:
            usuario.saldo -= monto
            self.saldo += monto
            print(f"Transferencia de {monto} desde {usuario.nombre} a {self.nombre} realizada.")


# Caso de uso
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)         # Bob: 70
alicia.transferir(bob, 80)     # Bob: -10... lanza error, saldo insuficiente
alicia.retirar_dinero(50)      # Alicia: 50     

