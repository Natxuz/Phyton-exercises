#conteo del numero total de vocales en una frase
frase = 'Using GitHub on Windows has never been this easy.'
vocales = 0

for letra in frase:
    letra = letra.lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o'  or letra == 'u':
        vocales += 1

print "La frase tiene " + str(vocales) + " vocales."