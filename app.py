from flask import Flask, render_template

import mysql.connector
# Conexión a la base de datos
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="root",
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
    query = "SELECT * FROM review"
    cursor.execute(query)
    reviews = cursor.fetchall()
    return render_template('sistema2.html', reviews=reviews)

@app.route('/hacerreview')
def hacerreview():
    return render_template('hacerreview.html')

@app.route('/eliminarreview')
def review():
    return render_template('eliminarreview.html')

@app.route('/verlibro')
def verlibro():
    query = "SELECT * FROM libro"
    cursor.execute(query)
    libros = cursor.fetchall()
    return render_template('VerLibro.html',libros=libros)

@app.route('/verpersonas', methods=['POST'])
def verpersonas():
    nombre_persona = request.form.get('persona')
    query = "SELECT * FROM usuario WHERE usuario.user_name"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    return render_template('verPersonas.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)