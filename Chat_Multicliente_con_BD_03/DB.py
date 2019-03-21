import mysql.connector

name_database = ''

def CREATE_DB(name):
    global name_database
    name_database = name
    conection = mysql.connector.connect( host="localhost", user="root", passwd="")
    cursor = conection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+name_database)

def CREATE_TABLE(table_db, column_table_db):
    global name_database
    conection = mysql.connector.connect( host="localhost", user="root", passwd="", database=name_database)
    cursor = conection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "+table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+column_table_db+" VARCHAR(255))")

def INSERT_DB(table_db, column_table_db, message_db):
    global name_database
    conection = mysql.connector.connect( host="localhost", user="root", passwd="", database=name_database)
    cursor = conection.cursor()
    cursor.execute("INSERT INTO "+table_db+" ("+column_table_db+") VALUES('"+message_db+"')")
    conection.commit()
    conection.close()

def SELECT_DB(table_db, column_table_db):
    global name_database
    conection = mysql.connector.connect( host="localhost", user="root", passwd="", database=name_database)
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM "+table_db)
    result = cursor.fetchall()
    return result
