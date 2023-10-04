def main ():
    def seleccion_sorf(Lista):
        n = len(Lista)
        for i in range(n):
            indiceMinimo = i
            for j in range(i + 1, n):
                if Lista[j] < Lista[indiceMinimo]:
                    indiceMinimo = j
                Lista[j],Lista[indiceMinimo] = Lista[indiceMinimo],Lista[j]

    mi_lista = [12, 32, 45,54,67,1,18]
    seleccion_sorf(mi_lista)
    print(mi_lista)

if __name__ == ("__main__"):
    main()