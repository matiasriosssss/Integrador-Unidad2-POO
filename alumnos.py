class Alumnos:
    __dni: int
    __ape: str
    __nom: str
    __carrera: str
    __anho: int   ## año que cursa

    def __init__(self, dni=0, apellido=None, nombre=None, carrera=None, anho=0):
        self.__dni = dni
        self.__ape = apellido
        self.__nom = nombre
        self.__carrera = carrera
        self.__anho = anho
    
    def __gt__ (self, x):
        primero = str (self.getAño()) + self.getNombre() + self.getApellido()
        segundo = str (x.getAño()) + x.getNombre() + x.getApellido()
        return primero > segundo

    def getDni (self):
        return self.__dni
    
    def getApellido (self):
        return self.__ape
    
    def getNombre (self):
        return self.__nom
    
    def getCarrera (self):
        return self.__carrera
    
    def getAño (self):
        return self.__anho