
class Camion:
    __Id = int
    __NombreConductor = str
    __patente = str
    __marca = str
    __tara = int

    def __init__(self, id, nombre, patente, marca, tara):
        self.__Id = id
        self.__NombreConductor = nombre
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara
    def getId(self):
        return self.__Id
    def getnombre(self):
        return self.__NombreConductor
    def getpatente(self):
        return self.__patente
    def gettara(self):
        return int(self.__tara)
