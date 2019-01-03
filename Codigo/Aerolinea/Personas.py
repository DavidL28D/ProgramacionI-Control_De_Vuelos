class Personas():

    def __init__(self, id, nombre, edad, vuelo, categoria):
        self.__id = id
        self.__nombre = nombre
        self.__edad = edad
        self.__vuelo = vuelo
        self.__categoria = categoria

    def mostrar(self):
        pass

    def calcularCategoria(self):
        pass

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getVuelo(self):
        return self.__vuelo
    
    def getCategoria(self):
        return self.__categoria

