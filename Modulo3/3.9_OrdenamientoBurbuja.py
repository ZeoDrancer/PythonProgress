def main():
    def burble_sorf(Lista):
        n = len(Lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if Lista[j] > Lista[j + 1]:
                    Lista[j], Lista[j + 1] = Lista[j + 1], Lista[j]

    Mi_lista = [ 12, 14 , 22, 15, 1, 78, 21, 2]
    burble_sorf(Mi_lista)
    print(Mi_lista)
    
if __name__ == ("__main__"):
    main()