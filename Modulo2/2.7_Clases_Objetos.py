#_-------------------------------Definicion de una clase--------------------------------
"""
Una clase en Python es una plantilla o un plano para crear objetos.
Define las propiedades y los comportamientos comunes que los objetos
de esa clase tendrán. Una clase se compone de atributos (variables) y
métodos (funciones).

class NombreDeClase:
# Definición de atributos
# Definición de métodos
"""

#Ejemplo de clase

class Persona: #Tiene 2 atributos edad y nombre

    def __init__(self, nombre, edad): #Metodo constructor, que seejecuta automáticamente al crear un objeto de la clase.
        self.nombre = nombre
        self.edad = edad
    def saludar(self): #Define el comportamiento de la clase
        print(f"Hola, mi nombre es{self.nombre}")
    def obtener_edad(self): #Define el comportamiento de la clase
        return self.edad
    
#_-------------------------------Definicion de un Objeto--------------------------------

persona = Persona("Ana", 25)

print(persona.nombre) #Se puede abseder a las caracteristicas del objeto persona
# Imprime "Ana"
persona.saludar()
# Imprime "Hola, mi nombre es Ana"
edad = persona.obtener_edad()
print(edad)
# Imprime 25

#Ejemplo 2

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")

producto1 = Producto("Camiseta", 25.99)
producto2 = Producto("Pantalón", 39.99)

producto1.mostrar_informacion()
producto2.mostrar_informacion()