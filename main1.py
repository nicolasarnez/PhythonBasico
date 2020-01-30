from vehiculo import Vehiculo
from motor import Motor
from simulador import Simulador

m1 = Motor ("897we",1000)
m2 = Motor ("78346",2000)

TataSport = Vehiculo ("7394","blanco","Tata","Sport2020","gasolina",732832,120,"si")
GreatWall2016 = Vehiculo ("6539","negro","GreatWall","2016","diesel",7349845,87,"no")
Jack2018 = Vehiculo ("7495","verde","Jack","2018","gasolina",7392,76,"no")

TataSport.poner_motor(m1)
GreatWall2016.poner_motor(m2)
Jack2018.poner_motor(m1)

lista = (TataSport,GreatWall2016,Jack2018)
s = Simulador(lista)

s.iniciar_simulacion (2)