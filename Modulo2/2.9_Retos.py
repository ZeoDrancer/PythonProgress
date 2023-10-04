"""
Ejercicio 1: Función de Saludo
Escribe una función saludo que acepte un argumento de nombre 
y retorne un saludo personalizado. Por ejemplo, saludo('Alice') 
debería retornar '¡Hola, Alice!'.
"""

#Solucion Ejercicio 1

"""
mensaje = input("Ingresa el mensaje personalizado: ")
nombre = input("Ingresa el Nombre de la persona que deseas saludar: ")

def Saludo(Nombre,Saludo):
    Mirar = print(f"{Saludo}, {Nombre}")
    return(Mirar)

llamado = Saludo(nombre,mensaje) #De esta manera me evito tener que hacer el print de lo que retorno
"""
"""
Escribe una función area_circulo que acepte un argumento de radio y 
calcule el área del círculo correspondiente. 
Recuerda que el área de un círculo se calcula como pi * radio**2.
"""

#Solucion Ejercicio 2

"""Radio = float(input("Ingrese el radio del círculo "))
def area_Circulo(radio):
    Area = 3.1416 * (radio**2)
    return(Area)

area_Total = area_Circulo(Radio)
print(f"El area total es: {area_Total:.2f}") 
"""

"""
Ejercicio 3: Conversor de temperatura
Escribe dos funciones, celsius_a_fahrenheit y fahrenheit_a_celsius, 
que conviertan temperaturas de una escala a otra.
"""

#Solucion Ejercicio 3

"""
def conversor_centigrados(grados):
    farehheit = (grados * (9/5))+32
    return(farehheit)

def conversor_farehheit(grados):
    centigrados = (grados - 32)/1.8
    return(centigrados)

def funcion():
    prediccion = input ("Seleccione la operacion que desea realizar. 1 Sí desea convertir de C° a F° o 2 Sí desea convertir de F° a C° ")
    return(prediccion)

Selecciones = ["1", "2", "3"]

while True:
    Selector = funcion()
    if Selector not in Selecciones:
        print ("Selección desconocida intente de nuevo")
    elif Selector == "1":
        print ("Converción de C° a F°")
        valor = float(input("Ingrese el valor en C° que desea pasar a F° "))
        convertidor = conversor_centigrados(valor)
        print(f"El resultado de C° a F° es: {convertidor:.2f}")
    elif Selector == "2":
        print ("Converción de F° a C°")
        valor = float(input("Ingrese el valor en F° que desea pasar a C° "))
        convertidor = conversor_farehheit(valor)
        print(f"El resultado de F° a C° es: {convertidor:.2f}")
    elif Selector == "3":
        break
"""
"""
Ejercicio 4: Función recursiva para cálculo de factorial
El factorial de un número n, denotado como n!, 
es el producto de todos los números enteros desde 1 hasta n. 
Escribe una función recursiva factorial que calcule el factorial de un número.
"""

#Solucion Ejercicio 4

"""
def factorial(factor): 
    Factor_Convertido = 1
    for i in range (1, (factor+1)):
        Factor_Convertido *= i
    return (Factor_Convertido)
    
valor = int(input("Ingrese el número entero del cual desea saber el factorial "))
llamado = factorial(valor)
print (f"El factorial de {valor} es {llamado}")
"""
"""
Ejercicio 5: Procedimiento de saludo
Escribe un procedimiento saludo_procedimiento 
que imprima un saludo personalizado en lugar de retornarlo. 
Por ejemplo, saludo_procedimiento('Alice') debería imprimir '¡Hola, Alice!'.
"""

#Solucion Ejercicio 5
"""
def Saludo(Saludo,Nombre):
    print(f"{Saludo} {Nombre}")

saludo_deseado = input("Ingrese el saludo que desea realizar ")
nombre_deseado = input("Ingrese el nombre de la persona que sea saludar ")

llamado = Saludo(saludo_deseado,nombre_deseado)
"""