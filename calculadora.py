class Calculadora:
    def __init__ (self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def sumar (self):
        try:
            suma = (self.numero1 + self.numero2)
            print ("la suma de {} y {} es ".format(self.numero1,self.numero2)+str(suma))
        except TypeError :
            print ("tipo de dato debe ser numerico")
        
    def restar (self):
        try:
            resta = (self.numero1 - self.numero2)
            print ("la resta de {} y {} es ".format(self.numero1,self.numero2)+str(resta))
        except TypeError :
            print ("tipo de dato debe ser numerico")
        
    def multiplicar (self):
        try:
            multiplica = (self.numero1 * self.numero2)
            print ("la multiplicaccion de {} y {} es ".format(self.numero1,self.numero2)+str(multiplica))
        except TypeError :
            print ("tipo de dato debe ser numerico")
            
    def dividir (self):
        try :
           dividi = (self.numero1 / self.numero2)
           print ("la division de {} y {} es ".format(self.numero1,self.numero2)+str(dividi))
        except ZeroDivisionError :
            print ("no se puede dividir entre cero")
        except TypeError :
            print ("tipo de dato debe ser numerico")
        except:
            print ("Error al dividir")
        
    def sacar_exponente (self):
        try:
            exponente = (self.numero1 ** self.numero2)
            print ("el exponente de {} y {} es ".format(self.numero1,self.numero2)+str(exponente))
        except TypeError :
            print ("tipo de dato debe ser numerico")