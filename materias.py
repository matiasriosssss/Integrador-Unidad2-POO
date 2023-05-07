class materiasAprobadas:
    __dni: int
    __nom: str #Nombre Materia
    __fecha: str
    __nota: int
    __aprob: str

    def __init__(self, dni, nom, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nom = nom
        self.__fecha = fecha
        self.__nota = nota
        self.__aprob = aprobacion

    def getDni (self):
        return self.__dni
    
    def getNombre (self):
        return self.__nom
    
    def getFecha (self):
        return self.__fecha
    
    def getNota (self):
        return self.__nota
    
    def getAprobacion (self):
        return self.__aprob