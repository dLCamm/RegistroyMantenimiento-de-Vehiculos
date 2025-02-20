import re
from os import system
from datetime import datetime
class Nodo:
    def __init__(self, valor): 
        self.Valor = valor
        self.Siguiente = None

class FlotaVehiculos:
    def __init__(self):
        self.Cabeza = None

    def Insertar(self, dato):
        Dato = Nodo(dato)

        if not self.Cabeza:
            self.Cabeza = Dato

        else:
            ahorita = self.Cabeza
            while ahorita.Siguiente:
                ahorita = ahorita.Siguiente
            ahorita.Siguiente = Dato

    def Mostrar(self):
        Ahorita = self.Cabeza
        while Ahorita:
            Ahorita.Valor.Imprimir()
            Ahorita = Ahorita.Siguiente
            
       

    def Buscar(self, buscando):
        Ahorita = self.Cabeza
        while Ahorita:
            if Ahorita.Valor.Placa == buscando:
                Ahorita.Valor.Imprimir()
                opcion = input("Presione 1 para agregar un nuevo mantenimiento a algún vehiculo, o 2 para Volver al menú: ")
                if (opcion == "1"):
                    Ahorita.Valor.History()

                else:
                    break
            elif Ahorita.Valor == None:
                print("Vehiculo no Encontrado")
                break
            else:
                Ahorita = Ahorita.Siguiente
    
    def Eliminar(self, eliminacion):
       

        if self.Cabeza.Valor.Placa == eliminacion:
            self.Cabeza = self.Cabeza.Siguiente
        else:
            Ahorita = self.Cabeza  
            while Ahorita:
                if Ahorita.Siguiente.Valor.Placa == eliminacion:
                    n = Ahorita.Siguiente
                    Ahorita.Siguiente = n.Siguiente
                    break
                
                else:
                    Ahorita = Ahorita.Siguiente

class Vehiculo:
    def __init__(self, marca, modelo):
        self.Placa = None
        self.Marca = marca
        self.Modelo = modelo
        self.Año = None
        self.Kilometraje = None
        self.Historial = FlotaVehiculos()
        self.total = 0
    
        
    def CostoTotal(self):
        total = 0
        actual = self.Historial.Cabeza
        while actual:
            total += actual.Valor.costo
            actual = actual.Siguiente
        print(f"     El costo total de servicios es de Q{total}")
        

    @property
    def año(self):
        return self.Año
    
    @año.setter
    def año(self, añ):
        if añ > 1900 and añ <= 2025:

            self.Año = añ
        
        else:
            print("El año no corresponde") 
            arreglar = int(input("Ingrese de nuevo el Año"))
            self.Año = arreglar

    @property
    def kilometros(self):
        return self.Kilometraje
      
    @kilometros.setter
    def kilometros(self, klometraje):
        if klometraje > 0:
            self.Kilometraje = klometraje
        else:
            print("El kilometraje no es positivo")
            arreglar = int(input("Ingrese de nuevo el Kilometraje: "))
            self.Kilometraje = arreglar

    @property
    def placa(self):
        return self.Placa
    @placa.setter
    def placa(self, plc):
        if re.fullmatch(r"\d{3}[A-Za-z]{3}", plc): #Este codigo es de una libreria, con el fin de darle formato a la placa de 3 numeros seguidos de 3 Letras
            self.Placa = plc
        else:
            print("La placa no corresponde, debe de ser 3 numeros seguidos de 3 letras")
            arreglar = input("Ingrese de nuevo la placa: ")
            self.Placa = arreglar
            
    def History(self):
        cuantos = int(input("Ingrese cuantos Mantenimientos va a agregar\n"))
        for i in range(0, cuantos):
            print("")
            print(f"Mantenimiento {i}")
            fecha = input("Ingrese fecha del Mantenimiento\n")
            descripcion = input("Ingrese una descripcion del Mantenimiento\n")
            costo = int(input("Ingrese el Costo del Mantenimiento\n"))
            nuevomantenimiento = Mantenimiento(fecha, descripcion, costo)
            self.Historial.Insertar(nuevomantenimiento)

            
        
    def Imprimir(self):
        print(f"El {self.Modelo} es de la Marca {self.Marca}, con Kilometraje de {self.Kilometraje}, del Año {self.Año}, con la Placa {self.Placa}")
        print("""     Estos son sus mantenimientos: """)
        actual = self.Historial.Cabeza
        while actual:
            print(f"""     El mantenimiento {actual.Valor.Descripcion} fue realizado la fecha {actual.Valor.Fecha}, por un valor de Q{actual.Valor.Costo} """)
            actual = actual.Siguiente
        self.CostoTotal()
        print(" ")
        
class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.Fecha = fecha
        self.Descripcion = descripcion
        self.Costo = costo        

    @property
    def fecha(self):
        return self.Fecha
    
    @fecha.setter
    def fecha(self, fecha):
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except:
            print("Formato de fecha incorrecto. Use YYYY-MM-DD.")
            arreglar = input("Ingrese de nuevo la fecha")
            self.Fecha = arreglar

    @property
    def costo(self):
        return self.Costo
    
    @costo.setter
    def costo(self, costo):
        if costo >= 0:
            self.Costo = costo
        else:
            arreglo = int(input("Error Costo negativo, volver a ingresar"))
            self.Costo = arreglo


listadevehiculos = FlotaVehiculos()

while True:
    system("cls")
    a = input("""Bienvenido
          Ingrese el número segun lo que desea realizar
          1. Agregar un Vehiculo
          2. Ver Vehiculos
          3. Buscar Vehiculo y su Información (Modificar)
          4. Eliminar un Vehiculo por su placa\n""")
    
    if (a == "1"):
        system("cls")
        placa = input("""Bienvenido a agregar un Vehiculo
              Ingrese Placa (Esta tiene que tener un formato de 3 Numeros seguidos de 3 Letras)\n""")
        marca = input("Ingrese la marca del Vehiculo\n")
        modelo = input ("Ingrese el Modelo del Vehiculo\n")
        añ = int(input("Ingrese el Año del vehiculo\n"))
        kilometraje = int(input("Ingrese el Kilometraje del Vehiculo\n"))
        nuevoauto = Vehiculo(marca, modelo)
        nuevoauto.año = añ 
        nuevoauto.placa = placa 
        nuevoauto.kilometros = kilometraje
        nuevoauto.History()
        nuevoauto.CostoTotal
        listadevehiculos.Insertar(nuevoauto)
        input("Vehiculo Agregado!!")

    elif (a == "2"):
        system("cls")
        listadevehiculos.Mostrar()
        input()

    elif (a == "3"):
        system("cls")
        buscando = input("Ingrese la placa del Vehiculo que Busca: ")
        listadevehiculos.Buscar(buscando)

    elif (a == "4"):
        system("cls")
        aeliminar = input("Ingrese la placa del Vehiculo que desea eliminar: ")
        listadevehiculos.Eliminar(aeliminar)
        input("Eliminado con exito")
    