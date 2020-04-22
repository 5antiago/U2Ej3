
class Cosecha():                                            
    __kilos = list 
    def __init__(self, camiones):                                    #Filas: Dias del mes  
        self.__kilos = [[0 for i in range(camiones)]for i in range(31)]   #Columna: id Camion 
    def agregarkilos(self, kilos, Camion, dia):
        if type(Camion) == int and type(dia) == int and type(kilos) == int:
            self.__kilos[dia-1][Camion-1] += kilos
    def getkilostotales(self, Camion):
        if type(Camion) == int:
            Camion -=1
            acum = 0
            for i in range(0, 31):
                acum += self.__kilos[i][Camion]
            return acum
        else:
            return -1
    def getkilosdia(self, dia, Camion):
        if type(Camion) == int and type(dia)== int:
            return self.__kilos[dia][Camion]
        else:
            return -1
    def testing(self):
        self.agregarkilos("f", 15, 2) #No se agrega parametro str no int
        self.agregarkilos(2000, 14, 6)
        print(self.getkilosdia(6-1, 14-1))
        print(self.getkilosdia(2-1, 15-1))
        print(self.getkilostotales(14-1))
        print(self.getkilostotales(15-1))
