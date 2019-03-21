import mysql.connector

nombre_db = ''

def CREATE_DATABASE(nombre):
    global nombre_db
    nombre_db = nombre
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="")
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+nombre_db)

def CREATE_TABLE(table_db, column_table_db, precio_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "+table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+column_table_db+" VARCHAR(255), "+precio_db+" INT(10))")

def INSERT_DATABASE(table_db, column_table_db, message_db, precio_db, valor_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO "+table_db+" ("+column_table_db+", "+precio_db+") VALUES('"+message_db+"', '"+valor_db+"')")
    conexion.commit()
    conexion.close()

def SELECT_DATABASE(table_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db)
    result = cursor.fetchall()
    return result
    # for x in result:
    #   print(x[1])

def UPDATE_DATABASE(table_db, producto_db, nombre_prod_db, precio_db, valor_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("UPDATE "+table_db+" SET "+producto_db+" = '"+nombre_prod_db+"', "+precio_db+" = "+valor_db+" WHERE id = "+code_db)
    conexion.commit()
    conexion.close()

def SELECT_WHERE_DATABASE(table_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db+" WHERE id = "+code_db)
    result = cursor.fetchall()
    return result

def DELETE_WHERE_DATABASE(table_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM "+table_db+" WHERE id = "+code_db)
    conexion.commit()
    conexion.close()
