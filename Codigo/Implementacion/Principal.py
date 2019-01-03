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
                    destino = palabra

                x += 1
                palabra = ""

            else:
                
                palabra += j
                
        viajes.append(Vuelo(nombre, int(vuelo), destino, int(palabra)))
    
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
        vuelo = int(vuelo)

        if categoria == 1:
            viajeros.append(Pasajero(id, nombre, edad, vuelo, categoria, polimorfismo, palabra))

        elif categoria == 2:
            viajeros.append(Azafata(id, nombre, edad, vuelo, categoria, float(polimorfismo), palabra))

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
    
    flag = False
    if tipo == "Nacional":
        print("Vuelos Nacionales")
        flag = True
    else:
        print("Vuelos Intenacionales")
    
    print("------------------------")
    print("ID - AEROLINEA - DESTINO")
    print("------------------------")

    for i in viajes:

        if flag and i.getTipo() == 1:
            print(i.getVuelo(),"-",i.getNombre(),"-",i.getDestino())

        elif not flag and i.getTipo() == 2:
            print(i.getVuelo(),"-",i.getNombre(),"-",i.getDestino())

    print()

def destinoFavorito():
    
    max = ["", 0, 0]
    cabezas = 0
    dinericos = 0
    
    for i in viajes:

        cabezas = 0
        dinericos = 0

        for j in viajeros:

            if ( i.getVuelo() == j.getVuelo() ) and j.getCategoria() == 1:

                cabezas += 1
                dinericos += j.getValorPasaje()

        if max[1] <= cabezas:
            max = [i.getDestino(), cabezas, dinericos]

    print("El destino favorito es:", max[0],"en el cual viajaron",max[1],"pasajeros y recaudó",max[2],"bolivares en pasajes\n")

def mejorPiloto():
    
    max = ["", 0]

    for i in viajeros:

        if i.getCategoria() == 3:
            
            if max[1] <= i.getHoras():
                max = [i.getNombre(), i.getHoras()]
    
    print("El piloto con mas horas de vuelo es:",max[0],"con",max[1],"horas registradas.\n")

def miniAzafata():

    min = ["", 9]

    for i in viajeros:

        if i.getCategoria() == 2:
            
            if min[1] >= float(i.getAltura()):
                min = [i.getNombre(), i.getAltura()]
    
    print("La azafata mas baja de altura es:",min[0],"con",min[1],"m.\n")
    