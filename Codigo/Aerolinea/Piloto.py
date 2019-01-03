from Aerolinea.Personas import *

class Piloto(Personas):

    def __init__(self, id, nombre, edad, vuelo, categoria, horas):

        super().__init__(id, nombre, edad, vuelo, categoria)
        self.__horas = horas

    def getHoras(self):
        return self.__horas

    def mostrar(self):

        self.calcularCategoria()

        print("Nombre:",self.getNombre(),"\nEdad:",self.getEdad(),"\nCategoria:",self.getCategoria(),"\nHoras de vuelo:",self.__horas)

    def calcularCategoria(self):

        # Para el piloto: si tiene más de 1500 horas de vuelo es “Capitán”, si tiene 1500 horas de vuelo o menos es “1er Piloto”

        c = ""

        if self.__horas > 1500:
            c = "Capitan"
        else:
            c = "Primer Piloto"
        
        self.setCategoria(c)