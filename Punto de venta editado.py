#!/usr/bin/env python3

# Projecto       : Punto de venta electronico

import pymysql

connection = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    port = 3306,
    password ="",
    db = "puntodeventas"


#Interfaz de usuario
PIN = "1234"
usuario = "Keiter" 
for i in range(3):
    entrada_2 = input("Indica tu usuario aqui:")
    entrada=input("Indica la contraseña para acceder: ")
    if entrada==PIN:
        break
    elif entrada_2 == usuario:
        break
if entrada_2 == usuario:
    print("Usuario correcto, Bienvenido Keiter sanchez")

else:
    print("usuario incorrecto")
if entrada==PIN:
    print("Contrasena correcta")
else:
    print("Su contrasena es incorrecta.")

# Definir funciones
def wait(t):
        for i in range(0,t):
                i = i + 0
                
def orderScreen(s): # Mostrar productos a la venta con precios.
        welcome = "     Bienvenido a la tienda de dulces JKD "
        instruct = "[P = Pagar] [Q = Quitar] | Por favor selecciona un producto."
        print("{:*^80}".format(welcome))
        
        for key in s.keys():
                print(u"{: >39} \xA3{: <39.2f}".format(key,s[key]))
                
        print("{:*^80}".format(""))
        print("{: ^80}".format(instruct))
        print("{:*^80}".format(""))

def acceptPayment(o,s):
        import time
        header = " Venta "
        prompt = u"{: >40}\xA3".format("Cantidad dada: ")
        total = 0.00
        given = 0.00
        change = 0.00
        
        for i in range(0,len(o)): # Calcular la deuda total.
                for key in s.keys():
                        if o[i] == key:
                                total = total + s[key]
        
        print("{:*^80}".format(header)) # Orden de impresión y monto adeudado.
        
        for i in range(0,len(o)):
                print(u"{: >39} \xA3{: <39.2f}".format(o[i],s[o[i]]))
                
        print(u"{: >40}\xA3{: <39.2f}".format("Monto adeudado: ",total))
        given = float(input(prompt)) # Cantidad dada.
        if given >= total: # Calcular el cambio adeudado.
                change = given - total
                print(u"{: >40}\xA3{: <39.2f}".format("Cambio devuelto: ",change))
        else:
                print("{: ^80}".format("Vuelve cuando puedas pagar."))
        time.sleep(3)

def takeOrder(s): # Consiga la orden de los clientes.
        kbd = ""
        order = []
        while str.upper(kbd) != "P": # Bucle hasta que el cliente decida pagar.
                if str.upper(kbd) == "Q": # Romper el bucle para quitar.
                        break 
                orderScreen(stock)
                kbd = input("::")

                for key in s.keys():
                        if key == str.capitalize(kbd):
                                order.append(str.capitalize(kbd))
                        
        if str.upper(kbd) == "P":
                acceptPayment(order,stock) # Llamar a aceptar Pago
                
        return kbd # Volver al programa principal.

# Variables del inventario 
stock = {"Skittles":0.50,"Gomitas":0.50,"Paletas":1.00,"Hershey":1.50,"MilkyWay":5.60} #La moneda esta en euros 

# Programa principal
kbd = ""
while str.upper(kbd) != "Q":
        kbd = takeOrder(stock)