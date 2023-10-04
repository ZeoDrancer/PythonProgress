#-------------------Definicion de diccionario---------------------
# Crear un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad":"Madrid"}
# Acceder a los valores del diccionario
nombre = mi_diccionario["nombre"]
edad = mi_diccionario["edad"]
# Modificar un valor del diccionario
mi_diccionario["ciudad"] = "Barcelona"
# Añadir un nuevo par clave-valor al diccionario
mi_diccionario["profesion"] = "Ingeniero"
# Eliminar un par clave-valor del diccionario
del mi_diccionario["edad"]
# Verificar si una clave existe en el diccionario
existe_ciudad = "ciudad" in mi_diccionario
# Número de pares clave-valor en el diccionario
num_pares = len(mi_diccionario)

#-------------------Definicion de Conjunto---------------------

# Crear un conjunto
mi_conjunto = {1, 2, 3, 4, 5}
# Añadir elementos al conjunto
mi_conjunto.add(6)
# Eliminar un elemento del conjunto
mi_conjunto.remove(3)
# Verificar si un elemento está en el conjunto
esta_presente = 4 in mi_conjunto
# Número de elementos en el conjunto
num_elementos = len(mi_conjunto)
