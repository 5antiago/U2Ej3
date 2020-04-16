import csv
from camion import Camion
from cosecha import Cosecha

def listado(Camiones, Cosechas):
    dia= int(input("Ingrese el dia: "))-1
    print("Patente \t Conductor \t Cantidad de Kilos \n")
    for i in range(len(Camiones)):
        kilos = Cosechas.getkilosdia(dia, i)
        if kilos !=0:
            print("{} \t {} \t {} \n ".format(Camiones[i].getpatente(), Camiones[i].getnombre(), kilos))


if __name__ == "__main__":
    Camiones = []
    with open("CAMIONES.csv") as archivo:
        reader = csv.reader(archivo, delimiter=(","))
        next(reader)                #Omite el header del archivo
        for row in reader:
            Camiones.append(Camion(int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))


    with open("COSECHAS.csv") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        next(reader)
        Cosechas = Cosecha(len(Camiones))
        for row in reader:
            Cosechas.agregarkilos(int(row[2])-Camiones[int(row[0])-1].gettara(),int(row[0]),int(row[1]))
    op = input(" 1. Cantidad de kilos del camion \n 2. Listado del dia \n 0. SALIR \nIngrese opcion: ")
    while( op !="0"):
        if op == "1":
            print("Total de Kilos: {}".format(Cosechas.getkilostotales(int(input("Ingrese Id del Camion: ")))))

        if op == "2":
            listado(Camiones, Cosechas)
        op = input(" 1. Cantidad de kilos del camion \n 2. Listado del dia \n 0. SALIR \nIngrese opcion: ")