import os
from menu import Menu
from manejadorAlumnos import manejadorAlumnos
from manejadorMaterias import manejadorMaterias

if __name__ == '__main__':
    manejador = '' ## manejador importado en main
    bandera = False
    menu = Menu()
    os.system('cls')
    while not bandera:
        menu.mostarMenu()
        opcion = int (input("Su opcion: "))
        mA = manejadorAlumnos (3,5)
        mM = manejadorMaterias ()
        menu.opcion(opcion, mA, mM)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')