def main():
    Productos = {'Manzanas' : 10,
                 'Peras': 5,
                 'Aguacates': 7,
                 'Mangos':8,
                 'Moras':20
                 }
    def buscar_inventario(accion, articulo,cantidad = 0):
        if accion == 'agregar':
            if articulo in Productos:
                Productos[articulo] += cantidad
            else:
                Productos[articulo] = cantidad
        elif accion == 'quitar':
            if articulo in Productos and Productos[articulo] >= cantidad:
                Productos[articulo] -= cantidad
            else:
                print("No se pudo realizar esta accion")
        elif accion == 'buscar':
            if articulo in Productos:
                return Productos[articulo]
            else:
                return None
        else:
            print("Accion no reconocida")

    buscar_inventario('agregar', 'Limones', 10)
    print(Productos)

    buscar_inventario('quitar', 'Aguacates', 3)
    print(Productos)

    print(buscar_inventario('buscar', 'Aguacates'))
  

if __name__ == ("__main__"):
    main()


