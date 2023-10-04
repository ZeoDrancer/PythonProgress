#-----------------------Declaracion de recursividad------------------------
#Calcular el resultado factorial de un numero
def funcion_recursiva(n):
# Caso base
    if n == 0:
        return 1
# Caso recursivo
    else:
        return n * funcion_recursiva(n - 1)
# Ejemplo de uso
numero = 5
resultado = funcion_recursiva(numero)
print(f"El resultado del factorial de {numero} es: {resultado}")

#Suma de los primeros números naturales

def suma_naturales(n):
 # Caso base
    if n == 0:
        return 0
 # Caso recursivo
    else:
        return n + suma_naturales(n - 1)
# Ejemplo de uso
numero = 5
resultado = suma_naturales(numero)
print(f"El resultado de la sumatorio de los números consecutivos hasta {numero} es: {resultado}")

#Permutaciones en una lista 

def permutaciones(Lista):
    if len(Lista) == 0:
        return []
    if len(Lista) == 1:
        return [Lista]
    lista_permutada = []
    for i in range(len(Lista)):
        m = Lista[i]
        lista_remanente = Lista[:i] + Lista[i+1:]
        for p in permutaciones(lista_remanente):
            lista_permutada.append([m]+p)
    return lista_permutada
    
Mi_lista = [ 1 , 2, 3, 4 ,5]
print(permutaciones(Mi_lista))



