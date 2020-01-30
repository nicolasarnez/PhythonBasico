class  Vehiculo:
    
    DISTANCIA_BASE = 12
    FACTOR_EMISION_GASOLINA = 2.196
    FACTOR_EMISION_DIESEL = 2.471
    
    def __init__ (self,placa,color,marca,modelo,combustible,Km,tanque,AC):
        self.placa = placa
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.Km = Km
        self.tanque = tanque
        self.AC = AC
        self.encendido = False
        self.litros_comsumidos = 0
        
    def encender(self):
        self.encendido = True
    
    def apagado (self):
        self.encendido = False
        
    def tocar_bocina (self):
        print ("muuuu")
        
    def frenar (self):
        print ("frenanado")
        
    def combustible (self):
        return (combustible)
    
    def mostrar_vehiculo (self):
        print ("Placa  " + str(self.placa))
        print ("Color  " + self.color)
        print ("Marca  " + self.marca)
        print ("Modelo  " + self.modelo)
        print ("combustible  " + self.combustible)
        print ("Km  " + str(self.Km))
        print ("Tanque  " + str(self.tanque))
        print ("Aire acondicionado  " + self.AC)
        
        if self.encendido == False:
           self:encendido = True
        else:
           print ("El vehiculo ya esta encendido")
     
    def cargar_combustible(self,litros):
        self.tanque += litros
        print (litros)
       
    def recorrer_distancia (self,distancia):
        if self.encendido:
             if distancia < (self.tanque * self.obtener_variante()):
                self.Km += distancia
                total_litros = round (distancia/self.obtener_variante())
                self.litros_comsumidos += total_litros
                self.tanque -= total_litros   
                print ("Recorriendo {} kilometros".format(distancia))
             else:
                print ("no tiene suficiente combustible")
        else:
            print ("vehiculo apagado")
            
    def calcular_co2():
        if self.combustible == "gasolina" :
            return self.FACTOR_EMISION_GASOLINA * self.litros_comsumidos
        else:
            return self.FACTOR_EMISION_DIESEL * self.litros_comsumidos
        
    def poner_motor (self,motor):
        self.motor = motor
        
    def obtener_variante (self):
        cilindrada = self.motor.obtener_cilindrada()
        if cilindrada == 1000:
           return (12)
        elif cilindrada == 2000:
            return (10)
        else:
            return (8)
    
    def hay_combustible (self,distancia):
        variante = self.obtener_variante()
        if not distancia < (self.obtener_variante() * self.tanque):
            return False
        else :
            return True
        
    def obtener_informe (self):
        informe = "\n----------------"
        informe +="INFORME FINAL-EMISION CO2"
        informe +="\n----------------"
        informe +="Ud esta conduciendo un vehiculo marca {},modelo {},color {}".format(self.marca,self.modelo,self.color)
        informe +="\n ha recorrido un total de {} Km de distancia".format(self.Km)
        informe +="\n ha consumido un total de {} litros de {}".format(self.litros_comsumidos,self.combustible)
        informe +="\n En su tanque tiene {} litros de {}".format(self.tanque,self.combustible)
        informe +="\n Se emitio a la atmosfera un total de {} Kg de CO2".format (round (self.calcular_co2(),2))
        return informe