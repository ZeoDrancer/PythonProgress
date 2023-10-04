"""Escriba un algoritmo para determinar si una palabra es un palíndromo. 
Un palíndromo es una palabra que se lee igual al revés que al derecho."""

def main():

    palabra = input("Ingrese la palabra para verificar sÍ es palíndromo: ").lower() #Se pide al usuario que ingrese una paabra que se volvera en minúscula
    salida = palabra == palabra[::-1] #se guarda la pabra en salida, comparando si su versión al reves es igual dando true o false
    if salida: #sí es verdadero
        print("La palabra", palabra,"es un palíndromo" )
    else: #sí es falso
        print("La palabra", palabra,"NO es un palíndromo" )


if __name__ == "__main__":
    main()