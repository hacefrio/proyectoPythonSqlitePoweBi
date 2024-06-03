import sqlite3
from datetime import datetime
import random
import graficos

# Crear la tabla ventas
def crear_tabla():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        producto TEXT,
        categoria TEXT,
        precio INTEGER,
        cantidad INTEGER,
        total INTEGER
    )
    ''')
    conn.commit()
    conn.close()

# Crear variable que guarda 50 productos, con sus respectivas categorías y precios
productos = [
    ('Notebook', 'Tecnologia', 1000),
    ('Tablet', 'Tecnologia', 500),
    ('Smartphone', 'Tecnologia', 300),
    ('Smartwatch', 'Tecnologia', 200),
    ('Television', 'Tecnologia', 1500),
    ('Heladera', 'Electrodomesticos', 2000),
    ('Lavarropas', 'Electrodomesticos', 1500),
    ('Microondas', 'Electrodomesticos', 500),
    ('Aspiradora', 'Electrodomesticos', 300),
    ('Cafetera', 'Electrodomesticos', 100),
    ('Zapatillas', 'Indumentaria', 200),
    ('Campera', 'Indumentaria', 500),
    ('Pantalon', 'Indumentaria', 300),
    ('Remera', 'Indumentaria', 100),
    ('Bufanda', 'Indumentaria', 50),
    ('Mesa', 'Muebles', 300),
    ('Silla', 'Muebles', 100),
    ('Sillon', 'Muebles', 500),
    ('Mesa de luz', 'Muebles', 50),
    ('Cama', 'Muebles', 1000),
    ('Cocina', 'Cocina', 500),
    ('Olla', 'Cocina', 100),
    ('Sarten', 'Cocina', 50),
    ('Cuchillo', 'Cocina', 20),
    ('Tenedor', 'Cocina', 10),
    ('Libro', 'Libreria', 50),
    ('Cuaderno', 'Libreria', 20),
    ('Lapicera', 'Libreria', 10),
    ('Goma', 'Libreria', 5),
    ('Regla', 'Libreria', 5),
    ('Bicicleta', 'Deportes', 500),
    ('Pelota', 'Deportes', 50),
    ('Raqueta', 'Deportes', 100),
    ('Botines', 'Deportes', 200),
    ('Camiseta', 'Deportes', 100),
    ('Pintura', 'Arte', 50),
    ('Pincel', 'Arte', 20),
    ('Lienzo', 'Arte', 100),
    ('Acrilico', 'Arte', 30),
    ('Oleo', 'Arte', 40),
    ('Guitarra', 'Musica', 300),
    ('Bateria', 'Musica', 500),
    ('Teclado', 'Musica', 200),
    ('Microfono', 'Musica', 100),
    ('Amplificador', 'Musica', 200),
    ('Cama', 'Mascotas', 100),
    ('Comedero', 'Mascotas', 20),
    ('Juguete', 'Mascotas', 10),
    ('Correa', 'Mascotas', 15),
    ('Collar', 'Mascotas', 15)
]

# Insertar datos al azar en la tabla ventas
def insertar_datos_aleatorios():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    print("¿Cuántos datos desea insertar?")
    cantidad = int(input())
    for _ in range(cantidad):
        indice = random.randint(0, 49)
        producto = productos[indice]
        cantidad_producto = random.randint(1, 10)
        total = cantidad_producto * producto[2]
        cursor.execute('''
            INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), producto[0], producto[1], producto[2], cantidad_producto, total))
    conn.commit()
    conn.close()

# Mostrar todos los registros de la tabla ventas
def mostrar_datos():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ventas')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
# metodo que exporte los datos a un archivo csv
def exportar_datos():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ventas')
    rows = cursor.fetchall()
    with open('ventas.csv', 'w') as file:
        # creaer encabezado
        file.write("id,fecha,producto,categoria,precio,cantidad,total\n")
        for row in rows:
            file.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
    print("Datos exportados correctamente")
    conn.close()
    
# Menú de opciones
def menu():
    print("\nMenú de opciones:")
    print("1. Crear tabla ventas")
    print("2. Insertar datos al azar en la tabla ventas")
    print("3. Mostrar datos")
    print("4. Exportar datos a un archivo CSV")
    print("5. Ver Graficos")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

# Función principal
def main():
    while True:
        opcion = menu()
        if opcion == "1":
            crear_tabla()
        elif opcion == "2":
            insertar_datos_aleatorios()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            exportar_datos()
        elif opcion == "5":
            graficos.menu()
        elif opcion == "6":
            break

    # Cerrar la conexión al finalizar
    conn.close()

if __name__ == '__main__':
    main()
