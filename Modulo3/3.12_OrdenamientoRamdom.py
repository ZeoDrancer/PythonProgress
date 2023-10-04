import random

numeros = [random.randint(1,100) for z in range(20)]
print(f"Lista desordenada {numeros}")

def burble_sorf(Lista):
        n = len(Lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if Lista[j] > Lista[j + 1]:
                    Lista[j], Lista[j + 1] = Lista[j + 1], Lista[j]


burble_sorf(numeros)
print(f"Lista Ordenada {numeros}")