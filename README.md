<p align="center">
  <img src="unet.png"/>
</p>

# Control_De_Vuelos
## Aplicación para control de vuelos orientado a objetos en Python

**NOTA: ESTA PRACTICA HA SIDO ADAPTADA A LENGUAJE PYTHON DEBIDO A QUE ORIGINALMENTE DEBIA SER DESARROLLADA EN JAVA**

El aeropuerto internacional Simón Bolívar desea llevar un registro y control de las personas que viajan en cada vuelo. Se desea registrar datos personales, categorías y datos del vuelo. Para llevar a cabo esta tarea se le proporcionará lo siguiente:

### Una clase llamada *Vuelos*, que se encuentra en el paquete *Aerolínea*, que contiene lo siguiente:

* Un atributo privado nombre de tipo String, que almacena el nombre de la aerolínea.
* Un atributo privado vuelo de tipo int, que guarda el número del vuelo.
* Un atributo privado tipo de tipo String, que indica si el vuelo es Nacional o Internacional.
* Un atributo privado destino de tipo String, que almacena la ciudad destino.
* Un constructor paramétrico que recibe los datos para inicializar todos sus atributos.
* Un método llamado mostrar que no recibe y retorna una cadena que contiene los datos del vuelo de la siguiente forma:<br><br>
“Aerolínea – Número del vuelo – Tipo del vuelo – Destino”<br><br>
* Los métodos getter para sus atributos.
* No contiene métodos setter.

### Una clase abstracta llamada *Personas*, que se encuentra en el paquete *Aerolínea*, que contiene lo siguiente:

* Un atributo privado id de tipo int, que almacena el N° de identificación de la persona.
* Un atributo privado nombre de tipo String, que almacena el nombre de la persona.
* Un atributo privado edad de tipo int, que guarda la edad de la persona.
* Un atributo privado vuelo de tipo int, que guarda el número del vuelo.
* Un atributo protegido categoría de tipo String, que almacena la categoría de la persona.
* Un constructor paramétrico que recibe los datos para inicializar todos sus atributos.
* Un constructor por defecto.
* Un método abstracto llamado mostrar que no recibe ni retorna ningún valor.
* Un método abstracto llamado calcularCategoría que no recibe ni retorna valores. Este método será implementado en las clases derivadas de la siguiente manera:<br><br>
    * Para los pasajeros: si el valor del pasaje es menor a 500 Bs su categoría es “Económica”, si está entre 501 y 650 es “Convenio” y si es mayor a 651 es “1era Clase”
    * Para las azafatas: si su edad <22 y habla  solo 2 idiomas es “Aprendiz”, si su edad es >=22 y habla máximo 3 idiomas es “Auxiliar”, si habla más de 3 idiomas es “Titular”
    * Para el piloto: si tiene más de 1500 horas de vuelo es “Capitán”, si tiene 1500 horas de vuelo o menos es “1er Piloto”<br><br>
* Los métodos getter para sus atributos.
* No contiene métodos setter.

### Una Interfaz llamada *Datos* que se encuentra en el paquete *Data* que contiene lo siguiente:

* Un atributo llamado "datos_vuelos" que es un vector de tipo String y contiene:<br><br>
* {"Conviasa;763;SC;1",”Conviasa;125;Porlamar;1","Aeropostale;815;Cancun;2","Conviasa;805;VAL;1","Aserca;725;Quito;2"}<br><br>
Este vector almacena la información de los vuelos en forma de cadena, y los atributos se encuentran delimitados por un “;”, el primer valor corresponde al nombre de la aerolínea, el segundo al número del vuelo, el tercero indica la ciudad destino y el cuarto indica el tipo de vuelo, 1 para Nacional y 2 para Internacional.<br><br>
* Un atributo llamado "datos_persona" que es un vector de tipo String y contiene:<br><br>
    * {"1;Jose Gonzalez;23;763;1;23A;550", "2;María Ramírez;19;125;2;1.65;3", "3;José Montoya;29;725;3;1350", "4;Gerardo Jaimes;25;805;3;2345", "5;Ana Pérez;36;815;2;1.72;4", "6;Emiro Martinez;33;815;1;5A;700", "7;Anabella Martinez;18;763;1;14C;320", "8;Mercedes Delgado;58;763;1;18D;440", "9;Diego Herrera;25;125;3;2445", "10;Cluadia Fernandez;47;763;1;6E;350"}<br><br>
Este vector almacena la información de los viajeros en forma de cadena, y los atributos se encuentran delimitados por un “;”, el primer valor corresponde al id , el segundo al nombre, el tercero indica la edad, el cuarto al número del vuelo, el quinto es un código que indica el tipo de persona (1 para Pasajero, 2 para Azafata y 3 para Piloto):<br><br>
        * En el caso de los pasajeros: el sexto corresponde a número de asiento y el séptimo al valor del pasaje.
        * En el caso de las azafatas: el sexto corresponde a estatura y el séptimo a la cantidad de idiomas.
        * En el caso de los pilotos: el sexto corresponde a horas de vuelo.

## Usted debe desarrollar lo siguiente:

### Una clase llamada *Pasajero* que se encuentra en el paquete *Aerolínea*  que debe heredar de Personas, y contiene lo siguiente:

* Un atributo privado numAsiento de tipo String, que almacena el N° de identificación del asiento.
* Un atributo privado valorPasaje de tipo int, que almacena costo en Bolívares del pasaje.
* Un constructor paramétrico que recibe los datos para inicializar todos los atributos (propios y heredados).
* Un constructor por defecto.
* Los métodos getter para sus atributos.
* No contiene métodos setter.
* Implementar el método mostrar de la Clase Persona que imprima por consola los datos como se presentan a continuación:<br><br>
    * Nombre: nombre<br>Edad: edad<br>Categoría: categoria<br>Asiento: numAsiento<br>Valor: valorPasaje<br><br>
* Implementar el método calcularCategoría de la Clase Persona que identifique la categoría del Pasajero y la asigne al atributo categoría.

### Una clase llamada *Azafata* que se encuentra en el paquete *Aerolínea*  que debe heredar de Personas, y contiene lo siguiente:

* Un atributo privado altura de tipo double, que almacena la estatura de la azafata.
* Un atributo privado idiomas de tipo int, que cantidad de idiomas que habla la azafata.
* Un constructor paramétrico que recibe los datos para inicializar todos sus atributos (propios y heredados).
* Los métodos getter para sus atributos.
* No contiene métodos setter.
* Implementar el método mostrar de la Clase Persona que imprima por consola los datos como se presentan a continuación:<br><br>
    * Nombre: nombre <br> Edad: edad<br>Categoría: categoria<br>Estatura: altura	<br>Idiomas: idiomas<br><br>
* Implementar el método calcularCategoría de la Clase Persona que identifique la categoría de la Azafata y la asigne al atributo categoría.

### Una clase llamada *Piloto* que se encuentra en el paquete *Aerolínea* que debe heredar de Personas, y contiene lo siguiente:

* Un atributo privado horas de tipo int, que almacena el N° de horas de vuelo.
* Un constructor paramétrico que recibe los datos para inicializar todos sus atributos (propios y heredados).
* Los métodos getter para sus atributos.
* No contiene métodos setter.
* Implementar el método mostrar de la Clase Persona que imprima por consola los datos como se presentan a continuación:<br><br>
    * “Nombre: nombre<br>Edad: edad<br>Categoría: categoria<br>Horas de vuelo: horas”<br><br>
* Implementar el método calcularCategoría de la Clase Persona que identifique la categoría del Piloto y la asigne al atributo categoría.

### Una clase llamada *Principal* en el paquete *Implementacion* que implemente la interfaz Datos y contenga lo siguiente:

* Un atributo viajes de tipo de Vuelo, donde se almacenaran los datos de los vuelos.
* Un atributo viajeros de tipo vector de Personas (vector de objetos polimórfico), donde se almacenaran los datos de los pasajeros y la tripulación(azafatas y pilotos).
* Un método llamado cargarDatos que no recibe ni retorna valores, el cual es el encargado de separar los datos de los vuelos y personas de los vectores datos_vuelos, datos_personas respectivamente, crear los objetos correspondientes y almacenarlos en los vectores.
* Un método llamado mostrarCategoría que no recibe ni retorna valores. Este método muestra organizadamente la información de los pasajeros y tripulantes,  debe indicar el valor de los atributos e indicar si es Pasajero, Azafata ó Piloto. Ejemplo:<br><br>
    * Pasajero<br>Nombre: Jose Gonzalez<br>Edad: 23<br>Categoría: 1era Clase<br>Asiento: 23A<br>Valor: 550<br><br>
* Un método llamado mostrarVuelos(String tipo) que no retorna valores y recibe el tipo de vuelo. Este método muestra tipo informe la información de los vuelos del tipo recibido. Ejemplo: Si se recibe “Nacional”<br><br>
    * Vuelos Nacionales<br>--------------------------<br>ID 	Aerolinea 	Destino<br>--------------------------<br>763 Conviasa SC<br>125 Conviasa Porlamar<br>805 Conviasa VAL<br><br>
* Un método llamado destinoFavorito que no recibe ni retorna valores. Este método muestra el destino que presente mayor número de pasajeros e indica el monto en Bs recaudado en pasajes.
* Un método llamado mejorPiloto que no recibe ni retorna valores. Este método muestra el nombre del Piloto que tiene mayor número de horas de vuelo registradas.
* Un método llamado miniAzafata que no recibe ni retorna valores. Este método muestra el nombre de la Azafata con estatura mas baja.
* El método main encargado de llamar a los métodos de una instancia de la clase principal.

**Nota: Los vectores datos_vuelos y datos_persona deben ser usados solo para cargar la información en el vector de objetos de viajes y de viajeros y no deben ser usados para realizar ningún otro cálculo.**

## Desarrollador
* [David Chacón (@DavidL28D)](https://github.com/DavidL28D)

*Proyecto desarrollado con propositos educativos para la **Universidad Nacional Experimental del Táchira***
