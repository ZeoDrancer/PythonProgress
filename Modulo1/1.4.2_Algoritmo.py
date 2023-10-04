"""
Algoritmo:
Leer el número desde el usuario.
Inicializar una variable booleana es_primo como verdadera.
Verificar si el número es menor o igual a 1. En ese caso, asignares_primo como falso.
Iterar desde 2 hasta la mitad del número (redondeando hacia arriba).
Si el número es divisible entre cualquier valor en ese rango, asignares_primo como falso y salir del bucle.
Si es_primo es verdadera, imprimir "El número es primo".
De lo contrario, imprimir "El número no es primo".
"""

numero = int(input("Ingrese un numero entero: "))
es_primo = True

if numero <= 1: #Si el numero es menor a 0 o igual a 1
    es_primo = False
else:
    for i in range(2, (numero // 2) + 1): #Iterar desde 2 hasta la mitad del número (redondeando hacia arriba).
        if numero % i == 0: # El // redondea la divicion al entero menor más cercano haci el decimal sea 0.9
            es_primo = False # if el mod de la divicion es 0 quiere decir que hay más divisores
            break

if es_primo: # Si es_primo es verdadera, imprimir "El número es primo".
    print("El número es primo.")
else:
    print("El número no es primo.")