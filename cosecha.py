
class Cosecha():                                            
    __kilos = list 
    def __init__(self, camiones):                                    #Filas: Dias del mes  
        self.__kilos = [[0 for i in range(camiones)]for i in range(31)]   #Columna: id Camion 
    def agregarkilos(self, kilos, Camion, dia):
        self.__kilos[dia-1][Camion-1] += kilos
    def getkilostotales(self, Camion):
        Camion -=1
        acum = 0
        for i in range(0, 31):
            acum += self.__kilos[i][Camion]
        return acum
    def getkilosdia(self, dia, Camion):
        return self.__kilos[dia][Camion]
        
