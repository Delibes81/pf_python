from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def obtener_datos(query, params=()):
    # Esta función obtiene los datos de la base de datos
    conn = sqlite3.connect('happyburger.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    conn.close()
    datos = [dict(zip(column_names, row)) for row in rows]
    return datos

@app.route('/')
def index():
    # Esta función renderiza la página de inicio
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    # Esta función renderiza la página de clientes
    query = 'SELECT * FROM clientes'
    datos = obtener_datos(query)
    return render_template('clientes.html', clientes=datos)

@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    # Esta función renderiza la página de pedidos
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
    # Esta función renderiza la página de menú
    query = 'SELECT * FROM menu'
    datos = obtener_datos(query)
    return render_template('menu.html', menu=datos)

if __name__ == '__main__':
    # Esta es la función principal que ejecuta la aplicación
    app.run(debug=True)