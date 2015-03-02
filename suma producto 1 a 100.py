# -*- coding: utf-8 -*-
# suma y producto de los numeros pares y los numeros impares entre 1 hasta 100.
limite = 100
a = 1
sumaPar = 0
sumaImpar = 0
productoPar = 1
productoImpar = 1
while a <= limite:
    if a % 2 == 0: #par, no tiene residuo
        sumaPar += a
        productoPar = productoPar * a
    else:   #impar, tiene residuo
        sumaImpar += a
        productoImpar = productoImpar * a
    a += 1
print "la sumatoria de los números pares es " + str(sumaPar)
print "la sumatoria de los números impares es " + str(sumaImpar)
print "La multiplicación de los números pares es " + str(productoPar)
print "La multiplicación de los números impares es " + str(productoImpar)