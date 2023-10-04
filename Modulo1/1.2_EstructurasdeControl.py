#-----------Estructura de control IF --------------
#ejemplo 1
numero = 10 

if numero > 0 :
    print("El numero es positivo") # imprime debido numero por ser mayor a 0

numero2 = -5

if numero2 > 0 :
    print("El numero es positivo") # imprime debido numero por ser mayor a 0
else:
    print("El numero es negativo")

#ejemplo 2

numero3 = 0

if numero3 > 0:
    print("El numero es positivo")
elif numero3  < 0:
    print("El numero es menor a 0")
else:
    print ("El numero es 0")

#-----------Estructura de iteracion While --------------

contador = 0

while contador <= 5:
    print(contador)
    contador += 1


#-----------Estructura de iteracion For--------------
#Ejemplo 1

Frutas = ["Naranja", "Melon", "Papaya", "Sandia"] #Esto se conoce como una lista

for fruta in Frutas: #fruta es un nombre de variable para recorer la lista de Frutas
    print(fruta)

for i in range (0,6):
    print(i)