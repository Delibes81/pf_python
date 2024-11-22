import sqlite3
import os

# Ruta de la base de datos
db_path = r'C:\Users\pascu\Documents\Python_tcmi\proyecto_final2'

# si la base de datos no existe se crea
if not os.path.exists(db_path):
    os.makedirs(db_path)

#concatena el nombre de la base de datos
db_path = os.path.join(db_path, 'happyburger.db')

# Conexión a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear tabla clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    clave TEXT PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    correo_electronico TEXT,
    telefono TEXT
)
''')

# Crear tabla menu
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (
    clave TEXT PRIMARY KEY,
    nombre TEXT,
    precio REAL
)
''')

# Crear tabla pedidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    pedido INTEGER PRIMARY KEY,
    cliente TEXT,
    producto TEXT,
    precio REAL,
    duracion TEXT
)
''')

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos y tablas creadas exitosamente.")