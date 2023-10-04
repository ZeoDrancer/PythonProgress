"""
Se quiere un programa que permita ingresar un numero de calificaciones, luego que calcule su promedio
"""

def main():
    Estudiante = input("Ingrese el nombre del estudiante: ")#Nombre del estudiante
    Calificaciones = []#Array para guardar las notas
    while True:
        Calificacion = float(input("Ingrese las calificaciones del estudiante: "))#Las calificaciones
        if Calificacion == 12345:#Condicion de salida ciclo While
            break
        elif Calificacion >= 5.1 or Calificacion < 0: #Conficion de restriccion ante el ingreso de las notas
            Calificacion = float(input("Calificación fuera de rango de evaluación, vuelva a ingresarla: "))
        else:
            Calificaciones.append(Calificacion)#Llenado del array con el metodo append

    average = sum(Calificaciones)/len(Calificaciones)#Calculo del promedio
    print("El promedio de notas de ",Estudiante,"es: ", average)



if __name__ == ("__main__"):
    main()