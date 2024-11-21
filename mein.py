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
    if path.exists("contador.txt"):
        contador = open("contador.txt", "r")
        numero = int(contador.read())
        contador.close()
        contador = open("contador.txt", "w")
        contador.write(str(numero+1))
        contador.close()
    else:
       print("No existe el archivo contador.txt")
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
                    linea_nueva += dato.lower()
                    linea_nueva += ",\n"
                    if path.exists("irregulares.txt"):
                        verbos = open("irregulares.txt", "a")
                        verbos.write(str(contador())+","+linea_nueva)
                        verbos.close()
                        print("Verbo agregado con éxito")
                else:
                    print("Debes ingresar el verbo en Español\n¡usando solo letras!")
            else:
                print("Debes ingresar el verbo en participio\n¡usando solo letras!")
        else:
            print("Debes ingresar el verbo en pasado\n¡usando solo letras!")
    else:
        print("Debes ingresar un verbo\n¡usando solo letras!")

def leer():
    if path.exists("irregulares.txt"):
        verbos = open("irregulares.txt", "r")
        print(f"\n{'#':<5}{'INFINITIVO':^10}{'PASADO':^10}{'PARTICIPIO':^10}{'ESPAÑOL':>10}")
        for verbo in verbos:
            lista = verbo.split(",")
            if len(lista) >= 5:
                print(f"{lista[0]:<5}{lista[1]:^10}{lista[2]:^10}{lista[3]:^10}{lista[4].strip():>10}") 
        verbos.close()
        print()
    else:
        print("No existe el archivo irregulares.txt")

def eliminar(numero):
    lista_verbos = []
    if path.exists("irregulares.txt"):
        verbos = open("irregulares.txt", "r")
        for verbo in verbos:
            lista = verbo.split(",")
            if lista[0] != str(numero):
                lista_verbos.append(lista)
        verbos.close()
         
    indice = 0
    for verbo in lista_verbos:
        verbo[0] = str(indice)
        indice += 1
    
    contador = open("contador.txt", "w")
    contador.write(str(indice))
    contador.close()

    verbos = open("irregulares.txt", "w")
    for verbo in lista_verbos:
        if verbo[0] != numero:
            verbos.write(verbo[0]+","+verbo[1]+","+verbo[2]+","+verbo[3]+","+verbo[4]+"\n")
    verbos.close
    print("Verbo eliminado exitosamente!")

def jugar():
    verbo_aleatorio = 0
    contador = open("contador.txt","r")
    verbo_aleatorio = random.randint(0,int(contador.read())-1)
    contador.close()

    if path.exists("irregulares.txt"):
        verbos = open("irregulares.txt", "r")
        for verbo in verbos:
            lista = verbo.split(",")
            if lista[0] == str(verbo_aleatorio):
                respuesta = input("Ingrese el infinitivo de " + lista[4].strip() + ": ")
                if respuesta.lower().strip() == lista[1]:
                    print("CORRECTO!")
                else:
                    print("INCORRECTO!") 
                respuesta = input("Ingrese el pasado de " + lista[4].strip() + ": ")
                if respuesta.lower().strip() == lista[2]:
                    print("CORRECTO!")
                else:
                    print("INCORRECTO!") 
                respuesta = input("Ingrese el participio de " + lista[4].strip() + ": ")
                if respuesta.lower().strip() == lista[3]:
                    print("CORRECTO!")
                else:
                    print("INCORRECTO!")
                break
        verbos.close()

def buscar(v):
    encontrado = False
    if path.exists("irregulares.txt"):
        verbos = open("irregulares.txt", "r")    
        for verbo in verbos:
            lista = verbo.split(",")
            if len(lista) >= 5:
                if lista[4].strip() == str(v):
                    encontrado = True
                    print(f"\n{'#':<5}{'INFINITIVO':^10}{'PASADO':^10}{'PARTICIPIO':^10}{'ESPAÑOL':>10}")
                    print(f"{lista[0]:<5}{lista[1]:^10}{lista[2]:^10}{lista[3]:^10}{lista[4].strip():>10}",end='')
        verbos.close()
        if not encontrado:
            print("En esta lista no tenemos el verbo " + v)

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