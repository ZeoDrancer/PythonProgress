# Programa principal
def main():
    from Geometria import calcular_area_rectangulo, calcular_area_circulo #Se importan las funciones desde Geometria.py
#Se pide al usuario que ingrese lo valores para calcular las areas correspondientes
#rectangulo
    base_rectangulo= float(input("Ingrese la base del rectangulo "))
    altura_rectangulo= float(input("Ingrese la altura del rectangulo "))
#círculo
    radio_circulo= float(input("Ingrese el radio del círculo "))
#Se asigna un valor
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    area_circulo = calcular_area_circulo(radio_circulo)
#Se imprime el valor retornado desde el archivo Geometria.py
    print("El área del rectángulo es:", area_rectangulo) 
    print ("El área del círculo es:", area_circulo)


if __name__ == ("__main__"):
    main()