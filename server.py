from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def obtener_datos(query, params=()):
    with sqlite3.connect('happyburger.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    query = 'SELECT * FROM clientes'
    datos = obtener_datos(query)
    return render_template('clientes.html', clientes=datos)

@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    mensaje = None
    if request.method == 'POST':
        pedido = request.form['pedidos']
        query = 'SELECT * FROM pedidos WHERE pedido = ?'
        datos = obtener_datos(query, (pedido,))
        if not datos:
            mensaje = f"El pedido con ID {pedido} no existe."
            query = 'SELECT * FROM pedidos'
            datos = obtener_datos(query)
        return render_template('pedidos.html', pedidos=datos, mensaje=mensaje)
    else:
        query = 'SELECT * FROM pedidos'
        datos = obtener_datos(query)
        return render_template('pedidos.html', pedidos=datos)

@app.route('/menu')
def menu():
    query = 'SELECT * FROM productos'
    datos = obtener_datos(query)
    return render_template('menu.html', productos=datos)

if __name__ == '__main__':
    app.run(debug=True)