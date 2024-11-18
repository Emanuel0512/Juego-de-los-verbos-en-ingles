import os
from os import path
import random

def crear():
    nombre = input("Ingrese el nombre del archivo nuevo que quiere crear: ").strip()
    nombre = nombre+".txt"
    if not path.exists(nombre):
        print("creando el archivo: " + nombre)
        open(nombre, "x")
    else:
        print("El archivo "+nombre+" ya existe")

def contador():
    numero = 0
    if path.exists("verbos.txt"):
        contador = open("verbos.txt", "r")
        numero = int(contador.read())
        contador.close()
        contador = open("contador.txt", "w")
        contador.write(str(numero+1))
        contador.close()
    else:
       print("No existe el archivo verbos.txt")
    return numero

def ingresar():
    linea_nueva = ""
    dato = input("Ingrese un verbo nuevo sin to: ").strip()

    if dato.isalpha():
        linea_nueva += dato.lower()
        linea_nueva += ","
        dato = input("Ingrese el mismoverbo en pasado: ").strip()
        if dato.isalpha():
            linea_nueva += dato.lower()
            linea_nueva += ","
            dato = input("Ingrese el mismo verbo en participio: ").strip()
            if dato.isalpha():
                linea_nueva += dato.lower()
                linea_nueva += ","
                dato = input("ingrese el mismo verbo en Español: ").strip()
                if dato.isalpha():
                    linea_nueva += dato
                    linea_nueva += ",\n"
                    if path.exists("irregulares.txt"):
                        verbos = open("irregulares.txt", "a")
                        verbos.write(str(contador())+","+linea_nueva)
                        verbos.close()
                else:
                    print("Debes ingresar el verbo en Español\n¡usando solo letras!")
            else:
                print("Debes ingresar el verbo en participio\n¡usando solo letras!")
        else:
            print("Debes ingresar el verbo en pasado\n¡usando solo letras!")
    else:
        print("Debes ingresar un verbo\n¡usando solo letras!")

def leer():
    print("Leyendo los verbos")

def eliminar(numero):
    print("Eliminando el verbo con numero " + str(numero))

def jugar():
    print("estamos jugando")

def buscar(v):
    print("Buscando el verbo " + v,"...") 

while True:

    opcion = input("\nEscriba: crear, para crear un archivo\n"+
                   "Escriba: ingresar, para ingresar un nuevo verbo\n"+
                   "Escriba: leer, para ver los verbos\n"+
                   "Escriba: eliminar, para eliminar un verbo\n"+
                   "Escriba: jugar, para jugar y practicar\n"+
                   "Escriba: buscar, para buscar un verbo\n"+
                   "Escriba: salir, para salir\n"+
                   "Opcion: ")
    
    opcion = opcion.lower().strip()

    if opcion == "crear":
        os.system('cls')
        crear()
    elif opcion == "ingresar":
        os.system('cls')
        ingresar()
    elif opcion == "leer":
        os.system('cls')
        leer()
    elif opcion == "eliminar":
        os.system('cls')
        numero = input("Escriba el numero del verbo que desea eliminar: ").strip()
        eliminar(int(numero))
    elif opcion == "jugar":
        os.system('cls')
        jugar()
    elif opcion == "buscar":
        os.system('cls')
        v = input("Ingrese el verbo que desea buscar: ").strip()
        buscar(v.lower())
    elif opcion == "salir":
        os.system('cls')
        break
    else:
        os.system('cls')
        continue