from Aerolinea.Personas import *

class Piloto(Personas):

    def __init__(self, id, nombre, edad, vuelo, categoria, horas):

        super().__init__(id, nombre, edad, vuelo, categoria)
        self.__horas = horas

    def getHoras(self):
        return self.__horas

    def mostrar(self):

        print("Nombre:",self.getNombre(),"\nEdad:",self.getEdad(),"\nCategoria:",self.calcularCategoria(),"\nHoras de vuelo:",self.__horas)

    def calcularCategoria(self):

        c = ""

        if self.__horas > 1500:
            c = "Capitan"
        else:
            c = "Primer Piloto"
        
        return c