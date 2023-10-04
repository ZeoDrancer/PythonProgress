#Pedir la masa en Kg

def main():

    Masa = float(input("Ingresa la masa en Kg: "))

    #Calcular la energia E = mc^2
    Constante = 3 * 10**6
    print(Constante)
    Energia = Masa * (Constante ** 2)

    print(f"Teniendo en cuenta que la masa es: {Masa} y que la constante es 3*10^6, la energia es: {Energia:.2f} Joulies")

if __name__ == ("__main__"):
    main()