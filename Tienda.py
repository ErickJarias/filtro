import json
import os

MY_REPERTORIO = "data/"
print("Bienvenido")
ID = int(input("Ingrese numero de identificación: "))
NOMBRE =input("ingrese nombre del producto1")

title = """
    ******************
    registrar producto
    ******************
    """
print(title)
MENU = ' \n1.producto1 \n2.producto2 \n3.salir'

criterio =(input("presiona enter para acceder"))
while (criterio):
    print(title)
    print(MENU)
    criterio=int(input('ingrese opcion:'))
    if criterio==1:
        print("producto2")
        cantidad  =int(input('ingrese cantidad de producto: '))
        precio =2000
        stockmax =20000
        total =cantidad*precio
        if total<20000:
            print('el precio a pagar es:',total)
            print('gracias por su compra')
        else:
            print('excede su compra; el stockmax es de:',stockmax)
            
            print(MENU(0))

    elif criterio == 2:
        print('producto2')
        ctd =int(input('Ingrese cantidad de producto:'))
        precio1=2500
        stockmax1=20000
        prec=ctd*precio1
        if prec<20000:
            print('el precio a pagar es:',prec)
            print('gracias por su compra')
        else:
            print('no puede exceder su compra, el stockmax es de:',stockmax1)
            MENU(0)
        
print('Upss. opcion invalida')
print('gracias por su compra')