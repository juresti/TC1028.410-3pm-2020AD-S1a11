import os
print(os.getcwd()) #donde trabaja Python

def pideDatos(nomArch):
    nombre = input("Dime tu nombre: ")
    edad = input("Dime tu edad: ")
    edoCivil = input("Dime tu estado civil: ")
    lista = [nombre + "\n", edad + "\n", edoCivil + "\n"]
    
    archivo = open(nomArch + ".txt","w")
    archivo.writelines(lista)
    archivo.close()
    print("Archivo escrito a disco")
    
def leeDatos(nombre):
    with open(nombre + ".txt","r") as archivo:
        for linea in archivo:
            print(linea)
