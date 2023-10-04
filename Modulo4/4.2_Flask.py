#Ejemplo de una instancia de proyecto en Flask
"""
from flask import Flask, render_template
# Crear una instancia de la aplicación
app = Flask(__name__)
# Definir una ruta y una función de vista
@app.route('/')
def index():
 return "¡Hola, mundo!"
# Iniciar la aplicación
if __name__ == '__main__':
 app.run()
"""
