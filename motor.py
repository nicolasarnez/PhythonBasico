class Motor:
    
    def __init__ (self,nro_serie,cilindrada):
        
        self.nro_serie = nro_serie
        self.cilindrada = cilindrada
        self.encendido_motor = False
            
    def encender(self):
        if self.encendido_motor == False :
            self.encendido_motor = True
        else:
            print ("El motor ya esta encendido") 
    
    def apagar(self):
        self.encendido_motor = False
        
    def esta_encendido (self):
        return (self.encendido_motor)
           
    def obtener_cilindrada(self):
        return (self.cilindrada)
        
    