import sqlite3
import inventory_app

conexion = sqlite3.connect('inventory.sqlite3')

products = inventory_app.inventory.get_products_in()

cursor = conexion.cursor()

cursor.execute('''
    INSERT INTO products (id_product, product, stock) 
    VALUES (?,?,?)
''', products)

conexion.commit()

cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall() 

for fila in resultados:
    print(fila)

conexion.close()