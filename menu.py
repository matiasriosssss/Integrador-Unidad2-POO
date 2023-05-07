import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            0: self.salir
                        }
        
    def opcion(self,op, mA, mM):   ##manejador == manejador de la clase enviada desde el main
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4:
            func(mA, mM)
        else:
            func()

    def mostarMenu(self):
        print("""
---------->Menu Principal<----------
-> 1: Cargar datos
-> 2: Mostrar promedio de un alumno
-> 3: Informar los estudiantes que aprobaron en forma promocional
-> 4: Obtener listado de alumnos
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self, mA, mM):
        os.system('cls')
        mA.carga()
        print(mA)
        mM.carga()
        #print (mM)

    def opc2 (self, mM):
        os.system('cls')
        print ('---------->Promedios<----------')
        dni = int (input ('ingrese dni del alumno a buscar: '))
        r = mM.promedioSinAplazo(dni)
        print (f'->dni: {dni}')
        print ('Promedio sin aplazos: {:.2f}'.format(r))
        r = mM.promedioConAplazo(dni)
        print ('Promedio con aplazos: {:.2f}'.format(r))

    def opc3 (self, mA, mM):
        os.system('cls')
        nom = str (input ('ingrese nombre de materia: '))
        mM.promocionales(nom, mA)

    def opc4(self, mA, mM):
        print ('---------->Alumnos<----------')
        os.system('cls')
        mA.ordenar()
        print (mA)

    def salir (self):
        print ('saliendo...')