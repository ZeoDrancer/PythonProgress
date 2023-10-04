#-------------------------Declaracion de la herencia-----------------------
"""
Para establecer una relación de herencia en Python, 
se utiliza la sintaxisde la definición de clase, 
con el nombre de la clase padre entreparéntesis 
después del nombre de la clase hija. A continuación, semuestra la sintaxis básica:

Herencia en Python

class ClaseHija(ClasePadre):
    # Definición de atributos y métodosadiionales
"""
#Ejemplo de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("¡Hola! Soy un animal.")

class Perro(Animal):
    def ladrar(self):
        print("¡Guau!")

perro = Perro("Fido")
print(perro.nombre) # Imprime "Fido"
perro.saludar() # Imprime"¡Hola! Soy un animal."
perro.ladrar() # Imprime "¡Guau!"

#Ejemplo de Polimorfismo

class Perro(Animal):
    def saludar(self):
        print("¡Guau! Soy un perro.")

class Gato(Animal):
    def saludar(self):
        print("¡Miau! Soy un gato.")
animal1 = Perro("Fido")
animal2 = Gato("Tom")
animal1.saludar() # Imprime "¡Guau! Soy unperro."
animal2.saludar() # Imprime"¡Miau! Soy ungato."