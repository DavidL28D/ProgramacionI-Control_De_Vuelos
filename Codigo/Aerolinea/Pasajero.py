from Aerolinea.Personas import *

class Pasajero(Personas):

    def __init__(self, id, nombre, edad, vuelo, categoria, numAsiento, valorPasaje):

        super().__init__(id, nombre, edad, vuelo, categoria)
        self.__numAsiento = numAsiento
        self.__valorPasaje = valorPasaje

    def getNumAsiento(self):
        return self.__numAsiento

    def getValorPasaje(self):
        return self.__valorPasaje

    def mostrar(self):

        self.calcularCategoria()

        print("Nombre:",self.getNombre(),"\nEdad:",self.getEdad(),"\nCategoria:",self.getCategoria(),"\nAsiento:",self.__numAsiento,"\nValor:",self.__valorPasaje)

    def calcularCategoria(self):

        precio = self.__valorPasaje

        if precio <= 500:
            c = "Economica"

        elif precio > 500 and precio <= 650:
            c = "Convenio"

        else:
            c = "Primera Clase"

        self.setCategoria(c)

    