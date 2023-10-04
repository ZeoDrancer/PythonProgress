#Ejemplo de contruccion de una app en PyWebIo
"""
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import input, TEXT
from pywebio.output import put_text
# Crear una instancia de la aplicación
app = Flask(__name__)
# Definir una ruta y una función de vista
@app.route('/')
def home():
 return send_from_directory(STATIC_PATH, 'index.html')
@app.route("/submit", methods=["POST"])
def submit():
 data = input("Ingresa tu nombre:", type=TEXT)
 put_text("¡Hola, {}!".format(data))
# Iniciar la aplicación
if __name__ == '__main__':
app.run(host='localhost', port=80)
"""