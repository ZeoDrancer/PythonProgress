"""
Implemente un programa que solicite al usuario el nombre de una variable en camel case y muestre
el correspondiente valor en snake case. Se supone que la entrada del valor sera en camel case
"""
def main():

    camelCase = input("Ingrese el nombre de la variable en camelCase: ")
    snake_case = ""

    for z in range(len(camelCase)): #len mide la longitud de la palabra en caracteres

        if camelCase[z].isupper(): #si la palabra en camel en la posicion de z es mayuscula
            snake_case += "_" + camelCase[z].lower() # añadale un guion y vuelve a ser minuscula
        else:
            snake_case += camelCase[z]#si no continua siendo la misma letra

    print("El nombre de la variable en snake_case es: ", snake_case) #muestra el resultado en snake_case

if __name__ == "__main__":
    main()

