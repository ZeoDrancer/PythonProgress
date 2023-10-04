"""
Supongamos que una maquina expendedora vende gaseosas a 50 centavos y solo acepta las siguientes denominaciones, 25 centavos, 10 y 5
implemente un programa que que permita al usuario ingresar una moneda
una vez haya obtenido minimo 50 centavos muestre la cantidad de centavos de cambio
"""

def main():

    Precio = 50
    Moneda_permitidas = [ 25, 10, 5]
    ingresado = 0
    dinero = Precio

    while dinero >= 0:
        moneda = int(input("Ingrese la moneda "))
        if moneda in Moneda_permitidas:
            ingresado += moneda
            dinero -= moneda
            print(f"El monto adeudado es: {ingresado} ")
        elif moneda not in Moneda_permitidas:
            print("Moneda no permitida, Intente de nuevo ")

    if ingresado >= Precio:
        cambio = ingresado - Precio
        print(f"El cambio es: {cambio} ")


if __name__ == ("__main__"):
    main()