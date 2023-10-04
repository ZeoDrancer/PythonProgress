def merge_sorf(Lista):
    if len(Lista) <= 1:
        return Lista
    medio = len(Lista) // 2
    izquierda = merge_sorf(Lista[:medio])
    derecha = merge_sorf(Lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and i < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i +=1
        else:
            resultado.append(derecha[j])
            j +=1
        
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

numeros = [34, 43,1,15,67,91,2]
ordenados = merge_sorf(numeros)
print(ordenados)
