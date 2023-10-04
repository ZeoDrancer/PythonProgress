
def main():

    def Busqueda(Lista, elemento): #Parametros la lista y el elemento
        for i in range(len(Lista)): #En el rango de la lista buscara
            if Lista[i] == elemento:#Si la lista en su recorrido es igual al elemento
                return i #Retornara el valor de i el cual sera tomado por llamado osea 4
        return -1 #Si no retornara -1
    
    Mi_Lista = [12,35,45,23,22,21,67]
    elemento_Buscado = 22

    Llamado = Busqueda(Mi_Lista, elemento_Buscado)
    if Llamado != -1:
        print(f"El elemento buscado {elemento_Buscado}, Se encontro en la posicion {Llamado}")
    else:
        print(f"El elemento buscado {elemento_Buscado}, NO se encontro ")

if __name__ == ("__main__"):
    main()