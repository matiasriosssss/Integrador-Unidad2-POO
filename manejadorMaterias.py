import csv
from materias import materiasAprobadas
from manejadorAlumnos import manejadorAlumnos

class manejadorMaterias:
    __listaMaterias = []

    def __init__(self):
        __listaMaterias = []
    
    def __str__(self):
        s = ""
        for i in range (len(self.__listaMaterias)):
            s += str(self.__listaMaterias[i].getDni()) + ',' + str(self.__listaMaterias[i].getNombre()) + ',' + str(self.__listaMaterias[i].getFecha()) + ',' + str(self.__listaMaterias[i].getNota()) + ',' + str(self.__listaMaterias[i].getAprobacion()) + '\n'
        return s

    def getLista(self):
        return self.__listaMaterias
    
    def carga (self):
        path = './materiasAprobadas.csv'
        archivo = open(path, 'r')
        reader = csv.reader (archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dni = int (fila[0])
                nombre = fila[1]
                fecha = fila[2]
                nota = int (fila[3])
                aprob = fila [4]
                xMateria = materiasAprobadas(dni, nombre, fecha, nota, aprob)
                self.__listaMaterias.append(xMateria)
        print ('carga de materias aprobadas lista')
        archivo.close()

    def buscarDni(self, dni):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(self.__listaMaterias):
            if self.__listaMaterias[indice].getDni() == dni:
                bandera=True
                valorDeRetorno=indice
            else: indice+=1
        if valorDeRetorno == None:
            print ('Error, Alumno no encontrado')
        return valorDeRetorno

    def promedioSinAplazo (self, dni):
        c = 0
        suma = 0
        for i in range (len (self.__listaMaterias)):
            if self.__listaMaterias[i].getDni() == dni and self.__listaMaterias[i].getNota() >= 4:
                suma += self.__listaMaterias[i].getNota()
                c = c + 1
        prom = suma / c
        return prom

    def promedioConAplazo (self, dni):
        c = 0
        suma = 0
        for i in range (len (self.__listaMaterias)):
            if self.__listaMaterias[i].getDni() == dni:
                suma += self.__listaMaterias[i].getNota()
                c += 1
        prom = suma / c
        return prom

    def promocionales (self, nom, mA):
        print ('_'*66)
        print ('|{:^10} {:^10} {:^10} {:^10} {:^10}|'. format('DNI', 'Nombre y Apellido', 'Fecha', 'Nota', 'Año que cursa'))
        print ('|----------------------------------------------------------------|')
        for materia in self.__listaMaterias:
            if nom == materia.getNombre() and materia.getAprobacion()=='P':
                d = materia.getDni()
                i = mA.buscarDni(d)
                alumno = mA.getAlumno(i)
                nya = alumno.getNombre() + alumno.getApellido()
                print ('|{:^10} {:^10} {:^10} {:^10} {:^10}|'. format(alumno.getDni(), nya, materia.getFecha(), materia.getNota(), alumno.getAño()))