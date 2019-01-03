class Vuelo():

    def __init__(self, nombre, vuelo, tipo, destino):
        self.__nombre = nombre
        self.__vuelo = vuelo
        self.__tipo = tipo
        self.__destino = destino

    def mostrar(self):

        print(self.__nombre, "", self.__vuelo, "", self.__tipo, "", self.__destino)

    def getNombre(self):
        return self.__nombre
    
    def getVuelo(self):
        return self.__vuelo

    def getTipo(self):
        return self.__tipo

    def detDestino(self):
        return self.__destino