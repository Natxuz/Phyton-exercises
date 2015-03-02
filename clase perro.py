# -*- coding: utf-8 -*-
#Definición de la clase PERRO
class perro:
#variables de las clases
    nombre = ""    
    edad = 0
    contacto = ""
    ladrido = ""
#Método principal    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def contacto(self):
        self.contacto = self.nombre, " tiene ", self.edad, " años."    

    def llamdo(self):
        self.ladrido = self.nombre, "hace guau guau guau"

#creación del objecto llamado Objeto a partir de la clase Perro                
objeto = perro("Camila", 5).contacto()
print objeto.contacto