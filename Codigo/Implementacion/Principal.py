from Data.Datos import *
from Aerolinea.Vuelo import *
from Aerolinea.Pasajero import *
from Aerolinea.Azafata import *
from Aerolinea.Piloto import *

viajes = []
viajeros = []

def cargaDatos():

    d = Datos()
    
    # Cargando vuelos
    for i in d.datos_vuelos:

        palabra = ""
        x = 0

        for j in i:

            if j == ";":

                if x == 0:
                    nombre = palabra

                elif x == 1:
                    vuelo = palabra

                elif x == 2:
                    tipo = palabra

                x += 1
                palabra = ""

            else:
                
                palabra += j
                
        viajes.append(Vuelo(nombre, vuelo, tipo, palabra))
    
    # Cargando viajeros
    for i in d.datos_personas:

        palabra = ""
        x = 0

        for j in i:

            if j == ";":

                if x == 0:
                    id = palabra

                elif x == 1:
                    nombre = palabra

                elif x == 2:
                    edad = palabra

                elif x == 3:
                    vuelo = palabra

                elif x == 4:
                    categoria = palabra
                
                elif x == 5:
                    polimorfismo = palabra
                
                x += 1
                palabra = ""

            else:
                palabra += j

        id = int(id)
        categoria = int(categoria)
        edad = int(edad)
        palabra = int(palabra)

        if categoria == 1:
            viajeros.append(Pasajero(id, nombre, edad, vuelo, categoria, polimorfismo, palabra))

        elif categoria == 2:
            viajeros.append(Azafata(id, nombre, edad, vuelo, categoria, polimorfismo, palabra))

        elif categoria == 3:
            viajeros.append(Piloto(id, nombre, edad, vuelo, categoria, palabra))

def mostrarCategoria():
    
    for i in viajeros:

        categoria = i.getCategoria()
        
        if categoria == 1:
            print("Pasajero:")

        elif categoria == 2:
            print("Azafata:")

        elif categoria == 3:
            print("Piloto:")

        i.mostrar()
        print()
        
def mostrarVuelos(tipo):
    pass

def destinoFavorito():
    pass

def mejorPiloto():
    pass

def miniAzafata():
    pass
    