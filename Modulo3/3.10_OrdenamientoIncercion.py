def main():
    def insertion_sorf(Lista):
        for i in range(1, len(Lista)):
            key = Lista[i]
            j = i - 1
            while j >= 0 and key <= Lista[j]:
                Lista[j +1] = Lista [j]
                j -= 1
            Lista[j + 1] = key

    Mi_lista = [13, 34,56,12,25,47,32,1]
    insertion_sorf(Mi_lista)
    print(Mi_lista)




if __name__ == ("__main__"):
    main()