def main():
    lista_compras = []
    while True:
        print("\n ---Lista de compras---")
        print("\n ---1. Agregar artículos---")
        print("\n ---2. Eliminar artículos---")
        print("\n ---3. Ver Lista---")
        print("\n ---4. Salir---")
        Selector = input("Por favor, elija que acción desea realizar ")
        if Selector == "1":
            item = input("Introduce el nombre del artículo para agregarlo: ")
            lista_compras.append(item)
        elif Selector == "2":
            item = input("Introduca el nombre del artículo que desea eliminar ")
            if item in lista_compras:
                lista_compras.remove(item)
        elif Selector == "3":
            print("\n Tu lista de compras es: ")
            for item in lista_compras:
                print(f"- {item}")
        elif Selector == "4":
            break
        else:
            print("Opcion ingresada es invalida ")


if __name__ == ("__main__"):
    main()