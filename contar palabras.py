# -*- coding: utf-8 -*-
#contar numero palabras de una cadena de caracteres basado en el numero de espacios en blanco
frase = '   We’ve made it easy to try out remote branches, create new local branches, and publish branches to share your work with others.   '
#Eliminación del exceso de espacios en blanco antes y despues de la frase.
frase = frase.lstrip()
frase = frase.rstrip()
print "La cantidad de palabras son: " + str(frase.count(" ", 1, len(frase)) + 1)