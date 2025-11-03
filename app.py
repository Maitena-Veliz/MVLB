from flask import Flask, render_template

import mysql.connector
# Conexión a la base de datos
conexion = mysql.connector.connect(
host="localhost",
user="usuario",
password="contraseña",
database="mvlb"
)
cursor = conexion.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sistema')
def sistema():
    return render_template('sistema.html')

@app.route('/sistema2')
def sistema2():
    return render_template('sistema2.html')

@app.route('/verlibro')
def verlibro():
    return render_template('VerLibro.html')

@app.route('/verpersonas')
def verpersonas():
    return render_template('verPersonas.html')

if __name__ == '__main__':
    app.run(debug=True)