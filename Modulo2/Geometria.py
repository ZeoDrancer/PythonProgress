# Módulo: geometria.py
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

"""
Legibilidad:
Al dividir un programa en módulos más pequeños yautónomos, 
facilitamos la lectura y la comprensión del código. 
Cadamódulo se enfoca en una tarea específica, lo que mejora 
la legibilidad yla claridad del programa.

Eficiencia:
Al reutilizar código existente en lugar de escribirlonuevamente, 
evitamos la duplicación y mejoramos la eficiencia.Podemos utilizar funciones,
procedimientos y módulos existentes pararealizar tareas comunes,
lo que ahorra tiempo y esfuerzo en eldesarrollo.

Mantenibilidad:
La modularidad y la reutilización de código facilitan elmantenimiento del programa.
Si se requiere un cambio en una función omódulo, 
solo es necesario modificarlo en un lugar y todos los lugaresdonde 
se utiliza se actualizarán automáticamente.

Extensibilidad:
Al utilizar la modularidad y la reutilización de código,
podemos construir programas que sean fácilmente extensibles. 
Sinecesitamos agregar nuevas funcionalidades, podemos desarrollarmódulos 
adicionales o extender los existentes sin afectar otras partesdel programa.
"""