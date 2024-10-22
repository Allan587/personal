import sqlite3
import inventory_app

conexion = sqlite3.connect('inventory.sqlite3')

cursor = conexion.cursor()

cursor.execute('''
    INSERT INTO usuarios (nombre, edad) 
    VALUES ('Juan', 30)
''')

conexion.commit()

cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall() 

for fila in resultados:
    print(fila)

conexion.close()