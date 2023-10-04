"""Escriba un algoritmo para calcular la factorial de un número. 
Recuerda que la factorial de un número n es el producto de todos los números 
enteros positivos desde 1 hasta n."""

def main():

    factorial = int(input("Ingrese el valor entero del numero al que desea conocer el factorial: "))
    resultado = 1
    for i in range(1,factorial+1):
        resultado *= i
    print("El factorial del numero ingresado es: ", resultado)


if __name__ == "__main__":
    main()