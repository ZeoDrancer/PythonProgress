def main():
    from Operaciones import Suma,Resta,Multiplicacion,Divicion

    print("Se revisaran los resultados entre 2 números para las diferentes operaciones basicas")
    numero1 = float(input("Ingrese el primer número "))
    numero2 = float(input("Ingrese el segundo número "))

    resultado_suma = Suma(numero1,numero2)
    resultado_resta = Resta(numero1,numero2)
    resultado_multiplicacion = Multiplicacion(numero1,numero2)
    resultado_divicion = Divicion(numero1,numero2)

    print(f"Con los numeros dijitados los cuales son: {numero1} y {numero2} los resultados obtenidos fueron")
    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicacion: {resultado_multiplicacion}")
    print(f"Divicion: {resultado_divicion:.2f}")

if __name__ == ("__main__"):
    main()