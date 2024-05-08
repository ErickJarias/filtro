import os

def convertidor_dolar ():
    pesos = int(input("ingrese la cantidad a cambiar en dolares"))
    dolar = 3944 
    conversion = pesos / dolar
    print(f"la cantidad de dolares que tiene es de {conversion}")
    menu(0)

def convertidor_pesos():
    euros = int(input("ingrese la cantidad a cambiar en euros"))
    pesos = 4279
    conversion = euros * pesos
    print(f"la cantidad de pesos que tiene es de {conversion}")
    menu(0)

def convertidor_euro():
    pesos = int(input("ingrese la cantidad a cambiar en pesos"))
    euros = 4279
    conversion = pesos / euros
    print(f"la cantidad de euros que tiene es de {conversion}")
    menu(0)

def convertidor_yen():
    pesos = int(input("ingrese la cantidad a cambiar en yenes"))
    yen = 26.30 
    conversion = pesos / yen
    print(f"la cantidad de yenes que tiene es de {conversion}")
    menu(0)

def menu(op=int):
      
    title = """
    ****************
    cambios finanzas  
    ****************
    """
    try:
        print (title)
        print("\n1.convertir pesos a dolares \n2. convertir pesos a Euros \n3.convertir euros a pesos \n4.convertir pesos a yenes \n5.salir ")
        op = int(input("ingrese la opcion que requiere: "))
    except: ValueError   
    match (op!=6):
       case 1:
          convertidor_dolar()
       case 2:
          convertidor_euro()
       case 3:
          convertidor_pesos()
       case 4:
          convertidor_yen()
       case 5:
          print("salir")
       case _:
          print("upss. opcion nno valida")
          menu(0)
menu(0)
           





