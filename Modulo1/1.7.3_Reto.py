"""Implementa un algoritmo que ordene una lista de números de menor a mayor. 
Puedes usar cualquier algoritmo de ordenación que prefieras."""

def main():

    numeros = [6, 8, 9, 4, 3, 1, 5] #Se pide al usuario que ingrese una paabra que se volvera en minúscula
    listaOrdenada = []
    for i in range (1,200):
        if i <= i+1:
            listaOrdenada[i] += numeros[i]
        elif i >= i+1:
            listaOrdenada[i]= numeros[i+1]
            i = 1
    print(listaOrdenada)

if __name__ == "__main__":
    main()