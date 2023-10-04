"""
1. Leer la base del triángulo desde el usuario.
2. Leer la altura del triángulo desde el usuario.
3. Calcular el área del triángulo utilizando la fórmula: área = (base *altura) / 2.
4. Mostrar el resultado del cálculo del área en la pantalla."""

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)