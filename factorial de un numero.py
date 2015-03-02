# -*- coding: utf-8 -*-
#Función factorial de un numero
def factorial(numero):
    temp = 0
    a = 2
    while a <= numero:
        print str(a) + " " + str(a-1)
        temp = a * (a - 1)
        a += 1
    return temp 
#Calculo del factorial de 5
a = 5    
b = factorial(a)
print "El factorial de " + str(a) + " es " + str(b)