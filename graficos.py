# clase para cerar graficos de las ventas de la base de datos
import matplotlib.pyplot as plt
import sqlite3

def crearGraficoPieVentasPorCategoria():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT categoria, SUM(total) as total
    FROM ventas
    GROUP BY categoria
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    categorias = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]

    def func(pct, allvals):
        absolute = int(pct/100.*sum(allvals))
        return "{:.1f}%\n({:d}$)".format(pct, absolute)
    
    plt.figure(figsize=(10, 6))
    plt.pie(totales, labels=categorias, autopct=lambda pct: func(pct, totales))
    plt.title('Ventas por categoría')
    plt.show()

    
def crearGraficoBarrasVentasPorCategoria():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT categoria, SUM(total) as total
    FROM ventas
    GROUP BY categoria
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    categorias = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.bar(categorias, totales)
    plt.title('Ventas por categoría')
    plt.show()

def crearGraficoBarrasVentasPorProducto():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT producto, SUM(total) as total
    FROM ventas
    GROUP BY producto
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    productos = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.bar(productos, totales)
    plt.title('Ventas por producto')
    plt.show()

def crearGraficoLineasVentasPorFecha():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT fecha, SUM(total) as total
    FROM ventas
    GROUP BY fecha
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    fechas = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.plot(fechas, totales)
    plt.title('Ventas por fecha')
    plt.show()

def crearGraficoBarrasVentasPorMes():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT strftime('%Y-%m', fecha) as mes, SUM(total) as total
    FROM ventas
    GROUP BY mes
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    meses = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.bar(meses, totales)
    plt.title('Ventas por mes')
    plt.show()
    
def crearGraficoBarrasVentasPorDia():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT strftime('%Y-%m-%d', fecha) as dia, SUM(total) as total
    FROM ventas
    GROUP BY dia
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    dias = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.bar(dias, totales)
    plt.title('Ventas por día')
    plt.show()

def crearGraficoBarrasVentasPorHora():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT strftime('%H', fecha) as hora, SUM(total) as total
    FROM ventas
    GROUP BY hora
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    horas = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.bar(horas, totales)
    plt.title('Ventas por hora')
    plt.show()

def crearGraficoPieVentasPorProductos():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT producto, SUM(total) as total
    FROM ventas
    GROUP BY producto
    ''')
    datos = cursor.fetchall()
    conn.close()
    
    productos = [dato[0] for dato in datos]
    totales = [dato[1] for dato in datos]
    
    plt.pie(totales, labels=productos, autopct='%1.1f%%')
    plt.title('Ventas por producto')
    plt.show()


def menu():
    print("\nMenú de opciones:")
    print("1. Crear gráfico de pie de ventas por categoría")
    print("2. Crear gráfico de barras de ventas por categoría")
    print("3. Crear gráfico de barras de ventas por producto")
    print("4. Crear gráfico de líneas de ventas por fecha")
    print("5. Crear gráfico de barras de ventas por mes")
    print("6. Crear gráfico de barras de ventas por día")
    print("7. Crear gráfico de barras de ventas por hora")
    print("8. Crear gráfico de pie de ventas por productos")
    print("9. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        crearGraficoPieVentasPorCategoria()
    elif opcion == "2":
        crearGraficoBarrasVentasPorCategoria()
    elif opcion == "3":
        crearGraficoBarrasVentasPorProducto()
    elif opcion == "4":
        crearGraficoLineasVentasPorFecha()
    elif opcion == "5":
        crearGraficoBarrasVentasPorMes()
    elif opcion == "6":
        crearGraficoBarrasVentasPorDia()
    elif opcion == "7":
        crearGraficoBarrasVentasPorHora()
    elif opcion == "8":
        crearGraficoPieVentasPorProductos()
    elif opcion == "9":
        return
    menu()

    