import datetime
from datetime import date
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, TH, FR
from holidays.constants import JAN, MAR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.constants import MON, WEEKEND
from holidays.holiday_base import HolidayBase
class FeriadoEcuador(HolidayBase):
    # https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_Colombia
    """
    FiestaEcuador(HolidayBase):

    La clase principal es (FeriadoEcuador) ya que seda el feriado en Ecuador 
    Su objetivo es determinar la fecha específica del dia de los feriados en el Ecuador
    https://www.turismo.gob.ec/wp-content/uploads/2020/03/CALENDARIO-DE-FERIADOS.pdf
    ...
    Atributos (Hereda la clase HolidayBase)
   
    """ 

    pais = "EC"
    """El def __init__(self, **kwargs): es un metodo para crear un objeto el **kwargs es para
    pasar los argumentos de la longitud de variables."""
    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)
    """El def _populate(self, year): es para cononcer el año actual"""
    def _populate(self, year):
        #==========================================
        #Año nuevo
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia del Año Nuevo que seria el 2022-01-01"""
        if self.observed and date(year, JAN, 1).weekday() in WEEKEND:
            self[date(year, JAN, 1)] = "Año Nuevo"
            pass
        else:
            self[date(year, JAN, 1)] = "Año Nuevo"
        #===============================================
        #Cantonización de la provincia de Santo Domingo
        #===============================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de Cantonización en Santo Domingo  que seria el 2022-07-03"""
        self[date(year, JUL, 3)] ="Cantonización de Santo Domingo"
        #==================================================
        #Provincialización de la provincia de Santo Domingo
        #==================================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de la Provincialización de Santo Domingo que seria el 2022-07-03"""
        self[date(year, NOV, 6)] ="Provincialización de Santo Domingo"

        #==========================================
        #Día del trabajador
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia del Trabajador que seria el 2022-05-01"""
        self[date(year, MAY, 1)] = "Dia del Trabajo"

        #==========================================
        #Día de San José
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia del Día de San José que seria el 2022-03-19"""
        name = "Día de San José"
        if date(year, MAR, 19).weekday() == MON or not self.observed:
            self[date(year, MAR, 19)] = name
        else:
            self[date(year, MAR, 19) + rd(weekday=MO)] = name 
        #==========================================
        #       Día de San Pedri y San Pablo
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de San Pedro y San Pablo que seria el 2022-07-04"""
        name = "San Pedro y San Pablo"
        if date(year, JUN, 29).weekday() == MON or not self.observed:
            self[date(year, JUN, 29)] = name
        else:
            self[date(year, JUN, 29) + rd(weekday=MO)] = name  
        #==========================================
        #Sagrado Corazón
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de Sagrado Corazón que seria el 2022-06-27"""
        name = "Sagrado Corazón"
        hdate = easter(year) + rd(days=+68)
        if hdate.weekday() == MON or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name
        #==========================================
        #Navidad
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de la Navidad que seria el 2022-12-25"""
        self[date(year, DEC, 25)] = "Navidad"
        #==========================================
        #Día de los reyes magos
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia del Día de los reyes magos que seria el 2022-01-10"""
        name = "Día de los Reyes Magos"
        if date(year, JAN, 6).weekday() == MON or not self.observed:
            self[date(year, JAN, 6)] = name
        else:
            self[date(year, JAN, 6) + rd(weekday=MO)] = name
        #==========================================
        #La asuncion de la Virgen
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de La Asunción de la Virgen que seria el 2022-08-15"""
        name = "La Asunción de la Virgen"
        if date(year, AUG, 15).weekday() == MON or not self.observed:
            self[date(year, AUG, 15)] = name
        else:
            self[date(year, AUG, 15) + rd(weekday=MO)] = name  

        #==========================================
        #Día de todos los Santos
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de los  Santos que seria el 2022-11-07"""
        name = "Día de Todos los Santos "
        if date(year, NOV, 1).weekday() == MON or not self.observed:
            self[date(year, NOV, 1)] = name
        else:
            self[date(year, NOV, 1) + rd(weekday=MO)] = name 
        #==========================================
        #Jueves Santo
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de Jueves Santos que seria el 2022-04-14"""
        
        self[easter(year) + rd(weekday=TH(-1))] = "Jueves Santo"
        #==========================================
        #Viernes Santo
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de Viernes Santo que seria el 2022-04-15"""
        self[easter(year) + rd(weekday=FR(-1))] = "Viernes Santo"
        #==========================================
        #Día de la raza
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de La Raza que seria el 2022-10-17"""
        name = "Día de la Raza"
        if date(year, OCT, 12).weekday() == MON or not self.observed:
            self[date(year, OCT, 12)] = name
        else:
            self[date(year, OCT, 12) + rd(weekday=MO)] = name  
        #==========================================
        #Ascensión del señor
        #==========================================
        """ Daremos a conocer el año el mes y el dia de los feriados para ello daremos a conocer 
        el año, el mes y el dia de Ascensión del señor que seria el 2022-05-30"""
        name = "Ascensión del señor"
        hdate = easter(year) + rd(days=+39)
        if hdate.weekday() == MON or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name 

print ("=============================================================")
print ("            LISTADO DE LOS FERIADOS  DEL ECUADOR             ")
print ("=============================================================")
"""Llamaremos a la calse principal que es FeriadoEcuador() y daremos a conocer los dias de los feriados"""
Imprimir=FeriadoEcuador()
for  (year, JAN) in FeriadoEcuador(years=2022).items():
    print(year, JAN)          
print ("============================================================")

#============================================================================================================

"""La clase principal es superCine"""
class superCine:
#=======================================#
    #Constructor 
    def __init__(self,nombre,cedula,nomPelicula,asiento,valor):
        """====================================================#
        Atributos"""
        self.atributo1=nombre
        self.atributo2=cedula
        self.atributo3=nomPelicula
        self.atributo4=asiento
        self.atributo5=valor
    
    def ventanilla():
        """Creamos una funcion llamada ventanilla() para conocer un menu de las opciones 
        de pelicula que tiene el cine y despues llamamos la funcion de asientos(): para 
        conocer los asientos disponibles despues de que colocamos el haciendo disponible
        para despues llamar una funcion registroVentanilla() donde  nos dira que ingresemos los
        datos del cliente."""
        seleccionVentanilla=0 #evalua el numero 
        while seleccionVentanilla!=5: 
            print ("====================================================================")
            print ("                 Vienvenido al Super Cine           ")
            print ("        Contamos con 5 peliculas de estreno del 2022")
            print ("====================================================================")
            print("1. SONIC 2 -->Tiene un precio de $6,25 ")
            print("2. LLAMAS DE LA VENGANZA --> Tiene un precio de $6,00")
            print("3. DOCTOR STRANGER --> Tiene un precio de $6,50")
            print("4. CAMINO DEL TERROR --> Tiene un precio de $4,50")
            print("5. SALIR")
            print("====================================================================")
            while True:
                try:        
                    seleccionVentanilla=int(input("Elegir una Opcion: "))
                except:
                    print("Error")
                else:
                    break
            if seleccionVentanilla == 1:
                print("Uste cliente a selccionado la opcion 2. de SONIC 2")
                superCine.asientos()
                superCine.registroVentanilla()
            if seleccionVentanilla == 2:
                print("Uste cliente a selccionado la opcion 2. de LLAMAS DE LA VENGANZA ")
                superCine.asientos()
                superCine.registroVentanilla()
            if seleccionVentanilla == 3:
                print("Uste cliente a selccionado la opcion 3. de  DOCTOR STRANGER ")
                superCine.asientos()
                superCine.registroVentanilla()
            if seleccionVentanilla==4:
                print("Uste cliente a selccionado la opcion 4. de CAMINO DEL TERROR")
                superCine.asientos()
                superCine.registroVentanilla()
            if seleccionVentanilla==5:
                print("Su salida fue exitosa")

    def asientos():
        """Declaramos la funcion de asientos(): donde daremos a conocer una funcion
        para conocer los accientos disponibles por medio de una matriz 
        que cuenta con una fila de del 0 hasta el  9 y columna del 0 hasta el 9"""
        matriz=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [9, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(0,10):
            print(matriz[i])
        
        while True:
            try:
                escojer_fila=int(input("Ingrese la fila de su aciento del 1 hasta el 9: "))
                while escojer_fila<1 or escojer_fila>9:
                    print("Error")
                    escojer_fila=int(input("Ingrese la fila de su aciento del 1 hasta el 9: "))

                escojer_columna=int(input("Ingrese la columna de su aciento del 1 hasta el 9: "))
                while escojer_columna<1 or escojer_columna>9:
                    print("Error")
                    escojer_columna=int(input("Ingrese la columna de su aciento del 1 hasta el 9: "))
            except:
                print("Intente de nuevo")
            else:
                break
        
        
        matriz[escojer_fila][escojer_columna]=1
        if  matriz [ escojer_fila ] [ escojer_columna ] ==  1 :
            print ( "Este asiento ya está reservado." )
        else:
            print ( "Este asiento esta vacio" )

    def registroVentanilla():
        """Damos a conocer la funcion registroVentanilla(): donde le decimos al
        usuario que ingrese sus datos personales y conocer los numeros de asiento
        que queremos elegir y colocar el valor del costo de las entradas"""
        print("================================================")
        print("                  Registro de Cuenta            ")
        print("================================================")
        """daremos a conocner registoVentanilla=superCine donde el superCine es la
        clase principales que llamaremos los atributos que tiene la clase. """
        while True:
            try:        
                registoVentanilla=superCine(str(input("Ingrese su nombre: ")),
                int(input("Ingrese Cedula: ")),
                str(input("Ingrese el nombre de la pelicula: ")),
                int(input("Ingrese el numero de asiento que desea sentarce: ")),
                float(input("Ingrese el valor de la pelicula: ")),
                )
            except:
                print("Error")
            else:
                break
        #INICIAR CESION DEL SISTEMA
        print("================================================")
        print("           SUS DATOS PERSONALES SON: ")
        print("================================================")
        print("Nombre: ",registoVentanilla.atributo1)
        print("CEDULA: ",registoVentanilla.atributo2)
        print("PELICULA: ",registoVentanilla.atributo3 )
        print("ASIENTO ",registoVentanilla.atributo4 )
        print("VALOR",registoVentanilla.atributo5 )
        print("================================================")
        """Daremos a conocer la fecha y hora del mes
        datetime.now() es para manipular la fecha y hora 
        el strftime es para calcular el tiempo de la hora local"""
        fechaActual=datetime.datetime.now()
        """'%d Día del mes como un número decimal con ceros. 
        %m Mes como un número decimal con ceros.
        %Y Año con siglo como número decimal
        %H Hora (reloj de 24 horas) como un número decimal con ceros.
        %M Minuto como un número decimal con ceros.
        %S Segundo como un número decimal con ceros. """
        fechaActual2=datetime.datetime.strftime(fechaActual,'%B/%m/%Y %H:%M:%S' )
        print("La fecha en que compro la entrada del cine fue: ",fechaActual2)
        print("Su Factura fue exitosa " )

    def appCine():
        """Para la funcion appCine() nos dara a conocer dos opciones donde la primera opcion
        es un registro para conocer nuestro  usuario y contraseña la segunda opcion es para 
        conocer """
        while(True!=6):
            print("====================== APP DE SUPER CINE ======================")
            print("1.- Registrarse")
            print("2.- Iniciar sesion")
            print("3.- SALIR")
            print("===============================================================")
            while True:
                try:        
                    opcC=int(input("Seleccione una respuesta: "))
                except:
                    print("Error")
                else:
                    break
            if opcC==1:
                #Registrar una cuenta en el sistema.
                print("===============================================================")
                print("                   REGISRARSE EN LA APP")
                print("===============================================================")
                #Creacion de usuario
                while True:
                    try:
                        nombreApp=input("Ingrese su nombre: ")
                        apellidoApp=input("Ingrese su apellido: ")
                        telefApp=input("Ingrese su numero de telefono (10 digitos): ")
                        while len(telefApp)<10 or len(telefApp)>10:
                            print("Error")
                            telefApp=input("Ingrese su numero de telefono (10 digitos): ")
                        correoApp=input("Ingrese su correo electronico de preferencia: ")
                        if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                            print("Correo correcto")
                        else:
                            print("Error")
                            correoApp=input("Ingrese su correo electronico de preferencia: ")
                            if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                print("Correo correcto")
                            else:
                                print("Error")
                                correoApp=input("Ingrese su correo electronico de preferencia: ")
                                if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                    print("Correo correcto")
                                else:
                                    print("Error")
                                    correoApp=input("Ingrese su correo electronico de preferencia: ")
                                    if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                        print("Correo correcto")
                                    else:
                                        print("Error")
                                        correoApp=input("Ingrese su correo electronico de preferencia: ")
                                        if "@hotmail.com" and "@gmail.com" and "@outlook.com" and "@yahoo.es" and "@espe.edu.ec" in correoApp:
                                            print("Correo correcto")
                                        else:
                                            print("Error")
                                            correoApp=input("Ingrese su correo electronico de preferencia: ")
                    except:
                        print("Ingrese los datos correctamente")
                    else:
                        break
                #poner en minusculas con lower()
                #Minusculas al nombre,apellido y utilzar 3 primeras variables y las 3 ultimos valores del telefono
                nombreAppCortado=nombreApp[0:3].lower()
                apellidoAppCortado=apellidoApp[0:3].lower()
                telefAppCortado=telefApp[7:10]
                print("El nombre de usuario creado con sus datos es el siguiente")
                #asignacion de los datos a la variable user
                user=nombreAppCortado+telefAppCortado+ apellidoAppCortado
                print("→ ", user)
                """El password  es la crear una contrasenia  """
                print("La contrasenia creada es la siguiente")
                password=apellidoAppCortado + nombreAppCortado + telefAppCortado
                print("→ ",password )
            elif opcC==2:
                #Inicio de sesion al cliente y le daremos las opciones de las peliculas y el registro del ciente
                print("=======================================================")
                print("                 INICIO DE SESION                      ")
                print("=======================================================")
                user2=input(print("Ingrese el usuario: "))
                print("=======================================================")
                if user2==user:
                    print("El usuario es correcto: ")
                    print("=======================================================")
                    password2=input(print("Ingrese su  contrasenia: "))
                    print("=======================================================")
                    if password2==password:
                        print("La contrasenia es correcta ")
                        """LLamamos la funcion de ventanilla() para registar el usuario conocer los asiento disponibles"""
                        superCine.ventanilla()

                    else:
                        print("La constrasenia es incorrecta")
                else:
                    print("El usuario o contrasenia es incorrecto")

            elif opcC== 3:
                print("Acaba de salir del Menu de la App")
            else:
                print("Error, vuelva a ingresar de nuevo")
        

def menu():
        """Creamos un funcion menú que cuenta con 3 opciones por medio del while ya que
        es la que nos evalúa una condición si es verdadera y en ese menú llamamos las 
        funciones correspondiente para que el usuario pueda adquirir su película por 
        medio de la ventanilla y la segunda opción es para registrar una cuenta en el 
        APP del super cine para que pueda adquirir su película por medio de la 
        aplicación del super cine."""
        seleccionMenu=0 #evalua el numero 
        """while es para evaluar una condicion  """
        while seleccionMenu!=3: 
            print ("====================================================================")
            print ("             Bienvenido Al super Cine Santo Domingo                 ")
            print ("====================================================================")
            print("1. Ventanilla para el Cliente " )
            print("2. APP del Super Cine")
            print("3. Salir")
            print ("====================================================================")
            """La variable seleccionMenu=int(input("Elegir una Opcion: ")) nos dara a conocer que si no 
            cumple la condicion nos dara a conocer que el ingresamos correctamente la opcion """
            while True:
                try:        
                    seleccionMenu=int(input("Elegir una Opcion correcta del 1 al 3: "))
                except:
                    print("Error")
                else:
                    break
            """el if nos dara a conocer de las opciones 1,2 y3 """
            if seleccionMenu == 1:
                superCine.ventanilla() #llamo  la funcion de  ventanilla()
            if seleccionMenu == 2:
                superCine.appCine() #llamo la funcion appCine()
            if seleccionMenu == 3:
                print("Acaba salir del Menu Principal. Vuelva Pronto!")

menu()