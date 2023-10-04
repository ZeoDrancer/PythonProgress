#Ejercicio Taqueria.py
#Se define el directorio para sacar los elementos o articulos que puede comprar el cliente

def main():
    
    menu = {
        "BAJA TACO": 4.00,
        "BURRITO": 7.50,
        "BOWL": 8.50,
        "NACHOS": 11.00,
        "QUESADILLA": 8.50,
        "SUPER BURRITO": 8.50,
        "SUPER QUESADILLA": 9.50,
        "TACO": 3.00,
        "TORTILLA SALAD": 8.00
    }
    ordenTotal = 0
    while True: #Mientras que sea verdadero para evitar un bule infinito se usa la declaracion Try Except
        try:
            item = input("Ingrese su Artículo deseado: ")
        except EOFError:
            break
        item = item.upper() #Funcion que toma lo digitado por el usuario y lo convierte en Mayúsculas
        if item in menu:
            ordenTotal += menu[item]
            print(f" Su factura va en: $ {ordenTotal:.2f} ")
        elif item == "CONTROL-D":
            print(f"El total de su compra es: $ {ordenTotal:.2f} ")
        else:
            print("Articulo Invalido")

if __name__ == "__main__":
    main()


