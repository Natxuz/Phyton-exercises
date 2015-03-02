#Invertir un texto suministrado
frase = 'GTCA'
#utilizando una lista se parte en letras la cadena de caracteres
lista = list(frase)

#mediante el uso del enroque se pasa a la variable AUX de forma temporal uno de los datos de la lista
aux = lista[0]
lista[0] = lista[1]
lista[1] = aux

aux = lista[3]
lista[3] = lista[2]
lista[2] = aux

print lista

print "Antes: " + frase + " despues: " + ''.join(lista)