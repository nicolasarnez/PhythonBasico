def mayordeedad (numero):
    if numero >= 18 :
        print ("es mayor de edad")
    else:
        print ("es menor de edad")

mayordeedad (6)      


def es_par():
    numero = int(input ("ingrese un numero  "))
    if numero % 2 == 0:
        print ("el numero es par")
    else :
        print ("el numer es impar")
        
es_par()



def valor_numero ():
    n = int(input ("ingrese un numero  "))
    if n > 0:
        print ("el numero es negativo")
    elif n == 0 :
        print ("el numero es cero")
    else:
         print ("el numero es positivo")
    
    valor_numero()
    
#
def conny():
    c = int(input ("dinero  "))
        
    if (c > 0) and (c < 6):
        print ("puede comprar caramelos")
        
    elif (c > 5) and (c < 11):
        print ("se puede comprar chocolates")
        
    elif (c > 10 ) and (c < 16):
        print ("se puede comoprar lo que sea")
        
conny()

#
      
def unocien ():
       for numero in range (1,100,1):
              print (numero)
unocien()

#
    
def nombres ():
       for nombre in "nicolas":
              print (nombre)
nombres()

#

def materias ():
      materias_reprobadas = ("Artes","Religion","Matematicas","E. Fisica","Quimica","Biologia","Termo dinamica")
      for año in materias_reprobadas:
           print (año)
       
materias()

#

def zoo ():
  animales = ("loro","vaca","pejelagarto","jirafa","peces","zorro")
  animal = input ("ingrese animal  ") 
  for anim in animales:
    if anim == animal:
      print ("tengo ese animal")
      return
    print("no tengo ese animal")
    return
zoo()

    