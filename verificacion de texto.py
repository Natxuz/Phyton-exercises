# -*- coding: utf-8 -*-
def verificacion(dato, dato2):
    #Verificacion de dos datos suministrados por teclado para identificar si ambos son del tipo texto
    salida =""
    if not (dato.isdigit() and dato2.isdigit()):
        salida = "Hay una cadena!"
    elif (dato.isdigit() and dato2.isdigit()):
        if dato > dato2:
            salida = "Es mayor"
        elif dato == dato2:
            salida = "son iguales" 
        else:
            salida = "Es menor"
    return salida
        
#captura de los datos suministrados por teclado.
varA = str(raw_input('Inserte un dato:'))
varB = str(raw_input('Inserte un dato 2:'))
#llamado de la función e impresión de los resultados.
print verificacion(varA, varB)