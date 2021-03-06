#-------------------------------------------------------------------------------------------------------
# Importacion para llamar el tiempo y la hora, tambien la enumeracion de un contenido de la lista
#-------------------------------------------------------------------------------------------------------
import time 
from xml.etree.ElementTree import Element
#-------------------------------------------------------------------------------------------------------
# Usó de listas para guradar los datos que se van a ingresar
#-------------------------------------------------------------------------------------------------------
listaClientes= []
listaTienda=[]
listaFecha=[]
listaHora=[]
listaCovid=[]
#-------------------------------------------------------------------------------------------------------
# Constructor de la clase clientes con sus respectivas atributos en parametros
#-------------------------------------------------------------------------------------------------------
class clientes:
        #-------------------------------------------------------------------------------------------------------
        # Metodos de la clase
        #-------------------------------------------------------------------------------------------------------
    def __init__(self, nombres, apellidos,pais, usuario, contrasena,cedula):
        self.nombres=nombres
        self.apellidos=apellidos
        self.pais=pais
        self.usuario=usuario
        self.contrasena=contrasena
        self.cedula=cedula
        #-------------------------------------------------------------------------------------------------------
        # Metodo para registrarse
        #-------------------------------------------------------------------------------------------------------

    def registrarse(self, cliente, clave ):
        self.cliente=cliente
        self.clave=clave
        repetirSesion=True
#-------------------------------------------------------------------------------------------------------
#  Condicion repetitiva
#-------------------------------------------------------------------------------------------------------
        while repetirSesion==True:
    #-------------------------------------------------------------------------------------------------------
    #  Condicion de relacion con tabla de verdad
    #-------------------------------------------------------------------------------------------------------
            if cliente==usuario and clave==contrasena:
                            print("Inicio de sesion aceptado")
                            print ("■-----------------------------------------------------------------■ ")
                        #-------------------------------------------------------------------------------------------------------
                        #  Cambio de valor de la variable para finalizar el condicional repetitivo
                        #-------------------------------------------------------------------------------------------------------
                            repetirSesion=False
            else:
                            print("Usuario o contrasena estan mal escritos, vuelva a ingresar")
                            print ("■--------------------------------------------------------------■") 
        #-------------------------------------------------------------------------------------------------------
        # Metodo para registrarse en una tienda
        #-------------------------------------------------------------------------------------------------------
    def iniciarTienda(self,nombreTienda):
        self.nombreTienda1=nombreTienda
        print ("Se ha registrado en la tienda ",nombreTienda) 
        #-------------------------------------------------------------------------------------------------------
        # Metodo para registrar su caso
        #-------------------------------------------------------------------------------------------------------
    def estado(self,cedula1):
        self.cedula1=cedula1
        condicion=True
    #-------------------------------------------------------------------------------------------------------
    #  Condicion repetitiva
    #-------------------------------------------------------------------------------------------------------
        while condicion==True:
            #-------------------------------------------------------------------------------------------------------
            #  Condicion de relacion
            #-------------------------------------------------------------------------------------------------------
            if cedula1=="normal" :
                print("Covid-19 normal")
                condicion=False
            elif cedula1=="caso":
                print("Caso de Covid-19") 
                condicion=False
            elif cedula1=="cercano":
                print("Caso cercano") 
                condicion=False
            else:
                print("No se encuentra")

#-------------------------------------------------------------------------------------------------------
# Constructor de la clase Tienda
#-------------------------------------------------------------------------------------------------------
class Tienda:
#-------------------------------------------------------------------------------------------------------
#  Metodos de la clase
#-------------------------------------------------------------------------------------------------------
    def __init__(self,telefono, gerente,caso):
        self.gerente=gerente
        self.caso=caso
        self.telefono=telefono

#-------------------------------------------------------------------------------------------------------
#  Informacion de lo que encapsula la variable
#-------------------------------------------------------------------------------------------------------
menuPrincipal = """
■------------------------------■ 
         MENU PRINCIPAL 
■------------------------------■
1: Cliente 
2: Tienda 
3: Administrador 
4: Salida
■------------------------------■ 
"""
#-------------------------------------------------------------------------------------------------------
#  Bandera de la condicion repetitiva
#-------------------------------------------------------------------------------------------------------
repetir=True
#-------------------------------------------------------------------------------------------------------
#  Condicion repetitiva
#-------------------------------------------------------------------------------------------------------
while repetir == True:
    print(menuPrincipal)
    opcion=int(input("Seleccione una opcion: "))
    #-------------------------------------------------------------------------------------------------------
    #  Condicion relacion
    #-------------------------------------------------------------------------------------------------------
    if opcion == 1:
#-------------------------------------------------------------------------------------------------------
#  Informacion de lo que encapsula la variable
#-------------------------------------------------------------------------------------------------------
        menuClientes="""
        ■------------------------------■ 
                Menu Clientes 
        ■------------------------------■
        1: Registro de cuenta al sistema
        2: Inicio de sesion
        3: Registarse en una tienda 
        4: Ver historial de las tiendas que ha visitado
        5: Ver estado
        6: Salir
        ■------------------------------■ 
        """
        #-------------------------------------------------------------------------------------------------------
        #  Bandera de la condicion repetitiva
        #-------------------------------------------------------------------------------------------------------
        repetirCliente=True
        #-------------------------------------------------------------------------------------------------------
        #  Condicion repetitiva
        #-------------------------------------------------------------------------------------------------------
        while repetirCliente==True:
            print(menuClientes)
            opcionCliente=int(input("Seleccione una opcion: "))
            #-------------------------------------------------------------------------------------------------------
            #  Condicion relacion
            #-------------------------------------------------------------------------------------------------------
            if opcionCliente == 1:
                    
                    print (" ■------------------------------------------------------------------■")
                    print ("                    Registro de cuenta al sistema ")
                    print (" ■------------------------------------------------------------------■")
                    #-------------------------------------------------------------------------------------------------------
                    #  Ingreso de datos
                    #-------------------------------------------------------------------------------------------------------
                    nombres=str(input("-. Ingrese sus nombres: "))
                    #-------------------------------------------------------------------------------------------------------
                    #  Agregacion de un dato a lista
                    #-------------------------------------------------------------------------------------------------------
                    listaClientes.append(nombres)
                    apellidos=str(input("-. Ingrese sus apellidos: "))
                    listaClientes.append(apellidos)
                    cedula=int(input("-. Ingrese su numero de cedula: "))
                    pais=str(input("-. Nacionalidad: "))
                    #-------------------------------------------------------------------------------------------------------
                    #  concatenacion de un cierto numero de caracteres de la cadena
                    #-------------------------------------------------------------------------------------------------------
                    usuario=nombres[0:3] + apellidos[0:3]
                    #-------------------------------------------------------------------------------------------------------
                    #  concatenacion de un cierto numero de caracteres de la cadena y transformacion de un int a string
                    #-------------------------------------------------------------------------------------------------------
                    contrasena=apellidos[0:4]+str(cedula)[0:4]
                    print (" ■------------------------------------------------------------------■")
                    print ("             DATOS DEL CLIENTE INGRESADOS")
                    print (" ■------------------------------------------------------------------■")
                        #-------------------------------------------------------------------------------------------------------
                        #  Imprime lo que contiene las variables
                        #-------------------------------------------------------------------------------------------------------
                    print("Nombres y Apellidos: " +nombres+" " +apellidos)
                    print("Nacionalidad: "+pais)
                    print("Usuario Creado: "+usuario)
                    print("Contrasena Creada: "+contrasena)
            elif opcionCliente==2:
                        print (" ■------------------------------------------------------------------■")
                        print ("                        Inicio de sesion ")
                        print (" ■------------------------------------------------------------------■")
                        #-------------------------------------------------------------------------------------------------------
                        #  Asignacion de una variable
                        #-------------------------------------------------------------------------------------------------------
                        cliente=str(input("Usuario: "))
                        clave=str(input("Contrasena: "))
                        #-------------------------------------------------------------------------------------------------------
                        #  Intanciamiento de un objeto a una subclase
                        #-------------------------------------------------------------------------------------------------------
                        accion=clientes(nombres, apellidos,pais, usuario, contrasena,cedula)
                        accion.registrarse(cliente, clave)       
            elif opcionCliente==3:

                    print (" ■------------------------------------------------------------------■")
                    print ("                        Registrarse en una Tienda ")
                    print (" ■------------------------------------------------------------------■")
                    print (" -. Mayorista de ropa ")
                    print (" -. Lianjo")
                    print (" -. Factory Five")
                    print (" -. Amy ")
                    nombreTienda=str(input("Ingrese a que tienda se quiere registrar: "))
                        #-------------------------------------------------------------------------------------------------------
                        #  Intanciamiento de un objeto a una subclase
                        #-------------------------------------------------------------------------------------------------------                    
                    accion1=clientes(nombres, apellidos,pais, usuario, contrasena,cedula)
                    accion1.iniciarTienda(nombreTienda)
                        #-------------------------------------------------------------------------------------------------------
                        #  Ingreso de datos a la lista
                        #-------------------------------------------------------------------------------------------------------
                    listaTienda.append(nombreTienda)
                        #-------------------------------------------------------------------------------------------------------
                        #  Comando para mostrar la hora y fecha actual y luego agregar a la lista
                        #-------------------------------------------------------------------------------------------------------
                    listaFecha.append(time.strftime("%d/%m/%y"))
                    listaHora.append(time.strftime("%H:%M:%S"))
                    print ("Se ha registrado en la tienda ",nombreTienda)                    
            elif opcionCliente==4:
                    print("■-------------------------------------------------------------■")
                    print("Nro.   Fecha       Hora         Tienda")
                    print("■-------------------------------------------------------------■") 
                        #-------------------------------------------------------------------------------------------------------
                        #  Condicional repetitivo con comando para enumerar lo que contiene la lista
                        #-------------------------------------------------------------------------------------------------------
                    for i, element in enumerate(listaTienda):
                        print(i+1,"   ",listaFecha[i]," ",listaHora[i],"  ",listaTienda[i])
                        print("■-------------------------------------------------------------■")
            elif opcionCliente==5:
                    cedula1=str(input("-. Ingrese si es normal, caso o cercano: "))
                    #-------------------------------------------------------------------------------------------------------
                    #  Ingreso de datos a la lista
                    #-------------------------------------------------------------------------------------------------------
                    listaCovid.append(cedula1)
                        #-------------------------------------------------------------------------------------------------------
                        #  Intanciamiento de un objeto a una subclase
                        #-------------------------------------------------------------------------------------------------------     
                    accion1=clientes(nombres, apellidos,pais, usuario, contrasena,cedula)
                    accion1.estado(cedula1)
            elif opcionCliente==6:
                print("Salida exitosa")
                        #-------------------------------------------------------------------------------------------------------
                        #  Cambio de valor en la variable para salir del condicional repetitivo
                        #-------------------------------------------------------------------------------------------------------     
                repetirCliente=False
            else:
                print("Error: Valor no existente en el menu")

    elif opcion == 2:
        print (" ■------------------------------------------------------------------■")
        print ("                        Estado")
        print (" ■------------------------------------------------------------------■")

        print("■-------------------------------------------------------------■")
        print("Nro.   Fecha       Hora      Cliente    Tienda")
        print("■-------------------------------------------------------------■")
        #-------------------------------------------------------------------------------------------------------
        #  Condicional repetitivo con comando para enumerar lo que contiene la lista por orden
        #-------------------------------------------------------------------------------------------------------     
        for i, element in enumerate(listaTienda):
            print(i+1,"   ",listaFecha[i]," ",listaHora[i],"  ",listaClientes[i][0:8],"  ",listaTienda[i])
            print("■-------------------------------------------------------------■")


    elif opcion == 3:
#-------------------------------------------------------------------------------------------------------
#  Listas creadas para guardar datos 
#-------------------------------------------------------------------------------------------------------
        listaTelefono1=[]
        listaGerente=[]
        listaTelefono=['0948346212','0986456542','09475345345','09456456234']
        #-------------------------------------------------------------------------------------------------------
        #  Ingreso de datos a los objetos
        #-------------------------------------------------------------------------------------------------------
        gerente=str(input("Nombre del gerente: "))
        telefono=str(input("Ingrese su numero: "))
        #-------------------------------------------------------------------------------------------------------
        #  Ingreso de datos a la lista
        #-------------------------------------------------------------------------------------------------------
        listaTelefono1.append(telefono)
        listaGerente.append(gerente)
        print (" ■------------------------------------------------------------------■")
        print ("                        Detalle Cliente")
        print (" ■------------------------------------------------------------------■")
        print ("Nro.   Cliente      Telefono     Estado    ")
        print ("■-------------------------------------------------------------■")
        #-------------------------------------------------------------------------------------------------------
        #  Condicional repetitivo con comando para enumerar lo que contiene la lista por orden
        #-------------------------------------------------------------------------------------------------------  
        for i, element in enumerate(listaTienda):
            print(i+1,"   ",listaClientes[i][0:8]," ",listaTelefono[i],"  ",listaCovid[i])
            print("■-------------------------------------------------------------■")
                        
            print (" ■------------------------------------------------------3------------■")
            print ("                        Detalle Gerente")
            print (" ■------------------------------------------------------------------■")
            print ("Nro.   Nombre      Telefono    Gerente     Estado    ")
            print ("■-------------------------------------------------------------■")
        #-------------------------------------------------------------------------------------------------------
        #  Condicional repetitivo con comando para enumerar lo que contiene la lista por orden
        #-------------------------------------------------------------------------------------------------------  
            for i, element in enumerate(listaTienda):
                            print(i+1,"   ",listaTienda[i]," ",listaTelefono[i],"  ",listaGerente[i]," ",listaCovid[i])
                            print("■-------------------------------------------------------------■")
    elif opcion == 4:
        print("Gracias ppor asistir")
        #-------------------------------------------------------------------------------------------------------
        #  Cambio de valor de la variable para el finalizar el condicional repetitivo
        #-------------------------------------------------------------------------------------------------------  
        repetir = False
    else:
        print("Teclado incorrecto")

