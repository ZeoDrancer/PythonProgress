#---------------------Declaracion de las funciones--------------------------
"""
def nombre_de_funcion(parametros):
# bloque de código de la función
# instrucciones a ejecutar
return valor_de_retorno
"""
#Ejemplo 1
def mirar(base, altura):
    area = base*altura
    return (area)
resultado = mirar(4, 10)
print(resultado) # Imprime 15

#Ejemplo 2
def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana") # Imprime "Hola, Ana", pero se puede cambiar el nombre en el parametro

#Ejemplo 3

def saludar(nombre, saludo):
    mensaje = saludo + ", " + nombre
    print(mensaje)#Como no hay una variable que almacene el retorno se imprime directamente 

saludar(nombre="Juan", saludo="Hola")#Imprime de acuerdo al orden en el cual se trataron los datos

#Ejemplo 4

def multiplicar(a, b):
    resultado = a * b
    return resultado

resultado =multiplicar(b = 5, a = 7)
print(resultado) # Imprime 35