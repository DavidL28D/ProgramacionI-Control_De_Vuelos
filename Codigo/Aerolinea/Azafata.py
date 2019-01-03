from Aerolinea.Personas import *

class Azafata(Personas):

    def __init__(self, id, nombre, edad, vuelo, categoria, altura, idiomas):

        super().__init__(id, nombre, edad, vuelo, categoria)
        self.__altura = altura
        self.__idiomas = idiomas

    def getAltura(self):
        return self.__altura

    def getIdiomas(self):
        return self.__idiomas

    def mostrar(self):

        self.calcularCategoria()

        print("Nombre:",self.getNombre(),"\nEdad:",self.getEdad(),"\nCategoria:",self.getCategoria(),"\nAltura:",self.__altura,"\nIdiomas:",self.__idiomas)
       
    
    def calcularCategoria(self):

        c = ""
        edad = self.getEdad()

        if edad < 22 and self.__idiomas <= 2:
            c = "Aprendiz"

        elif edad >= 22 and self.__idiomas <=3:
            c = "Auxiliar"

        elif self.__idiomas > 3:
            c = "Titular"

        else:
            c = "Sin categoria"
            
        self.setCategoria(c)