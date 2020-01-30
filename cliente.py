class Cliente:
    def __init__ (self,nombre,edad,talla,telefono,correo,comentario):
        self.nombre = nombre
        self.edad = edad
        self.talla = talla
        self.telefono = telefono
        self.correo = correo
    
    def mostrar_cliente (self):
        print ("Nombre  " + self.nombre)
        print ("Edad  " + str(self.edad))
        print ("Talla  "+ self.talla)
        print ("Telefono  "+ str(self.telefono))
        print ("correo  "+ self.correo)