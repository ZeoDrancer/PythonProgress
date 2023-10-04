"""
Realizar una calculadora de IMC(Indice de Masa Corporal)
"""

def main():

    Peso = float(input("Ingrese su masa corporal en Kg "))
    Altura = float(input("Ingrese su altura en metros "))

    IMC = Peso / (Altura**2)
    if IMC < 18.5:
        Resutado = "Bajo de peso"
        print("Estas bajo de peso")
    elif IMC >= 18.6 and IMC <= 25:
        Resutado = "Peso normal"
    else:
        Resutado = "Sobrepeso"
    
    print(f"Usted tiene un IMC de: {IMC:.1f} por lo tanto, esta en {Resutado}")
if __name__ == ("__main__"):
    main()