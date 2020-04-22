import csv
from camion import Camion
from cosecha import Cosecha
from manejadorcamiones import Manejacamiones

def listado(Camiones, Cosechas):
    dia= int(input("Ingrese el dia: "))-1
    print("Patente \t Conductor \t Cantidad de Kilos \n")
    for i in range(Camiones.cantcamiones()):
        kilos = Cosechas.getkilosdia(dia, i)
        if kilos !=0:
            print("{0:9} \t {1:15} \t {2:6} \n ".format(Camiones.getpatente(i+1), Camiones.getnombre(i+1), kilos))


if __name__ == "__main__":
    Camiones = Manejacamiones()
    Camiones.testing()
    with open("CAMIONES.csv") as archivo:
        reader = csv.reader(archivo, delimiter=(","))
        next(reader)                #Omite el header del archivo
        for row in reader:
            Camiones.agregacamion(Camion(int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))


    with open("COSECHAS.csv") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        next(reader)
        Cosechas = Cosecha(Camiones.cantcamiones())
        for row in reader:
            Cosechas.agregarkilos(int(row[2])-Camiones.obtenertara(int(row[0])),int(row[0]),int(row[1]))
     #menu       
    op = input(" 1. Cantidad de kilos del camion \n 2. Listado del dia \n 0. SALIR \nIngrese opcion: ")
    while( op !="0"):
        if op == "1":
            print("Total de Kilos: {}".format(Cosechas.getkilostotales(int(input("Ingrese Id del Camion: ")))))

        if op == "2":
            listado(Camiones, Cosechas)
        op = input(" 1. Cantidad de kilos del camion \n 2. Listado del dia \n 0. SALIR \nIngrese opcion: ")