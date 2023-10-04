"""Implementa un programa que solicite al usuario una cadena de texto y luego muestre esa cadena.
 pero sin las bocales (A,E,I,O,U), Ya sea que las ingresaron minúsculas o mayúsculas"""

def main():

    cadena = input("Ingrese una cadena de caracteres: ") #Se definio la cadena de caracteres
    resultado = twrrt(cadena) #se creo una funcion la cual sera llamada por resultado
    print("La palabra aveviada es:" +''.join(resultado)) #se imprime el valor de resultado
    
def twrrt(palabra): #cuando llaman a la funcion esta retornara la palabra
    palabra = palabra.lower() #se declara la palabra y se le asigna en minusculas con uppper es mayusculas
    salida=[] #se asigna la salida
    for z in range(len(palabra)): # for que recorrera el tamaño de la palabra para eso el lenth
        if palabra[z] not in [ "a", "e", "i", "o", "u", " "]: #si z no esta en la lista hara el append
            salida.append(palabra[z])#la palabra se guardara con el valor de z
    return salida#al terminar el for se retorna la palabra a donde fue llamada la funcion es decir a resultado
    
if __name__ == "__main__": #para que no llamen el archivo desde otro archivo
    main()