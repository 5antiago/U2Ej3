import camion

class Manejacamiones:
    __camiones = list
    def __init__(self):
        self.__camiones= []
    def agregacamion(self, uncamion):
        if type(uncamion) == camion.Camion:
            self.__camiones.append(uncamion)
    def obtenertara(self, id):
        if type(id)==int:
            return self.__camiones[id-1].gettara()
    def getpatente(self, id):
        if type(id)==int:
            return self.__camiones[id-1].getpatente()
    def getnombre(self, id):
        if type(id)==int:
            return self.__camiones[id-1].getnombre()
    def cantcamiones(self):
        return int(len(self.__camiones))
    def testing(self):
        self.agregacamion("camion") #No se agrega
        print(self.cantcamiones())
        self.agregacamion(camion.Camion(1, "testname", "AA 111 AA", "marcatest", 20000)) #Se agrega
        print(self.cantcamiones())
        print(self.getnombre(1))
        print(self.getpatente(1))
        print(self.obtenertara(1))