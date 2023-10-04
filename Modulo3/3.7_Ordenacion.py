#-------------------------Ordenacion---------------------------
#----------------------Metodo de la Burbuja--------------------

def ordenacion_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] =  lista[j + 1], lista[j]
# Ejemplo de uso
mi_lista = [4, 2, 6, 1, 8, 3]
ordenacion_burbuja(mi_lista)

#----------------------Metodo de la insercion--------------------
def ordenacion_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_actual
# Ejemplo de uso
mi_lista = [4, 2, 6, 1, 8, 3]
ordenacion_insercion(mi_lista)
