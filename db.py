import sqlite3
from sqlite3 import Error

def conectar():
    try:
        con = sqlite3.connect('db/datos.db')
        return con
    except Error as error:
        print(str(error))
        return None

def insert(_sql, lista):
    try:
        con = conectar()
        if con:
            ob_cursor = con.cursor()
            filas = ob_cursor.execute(_sql, lista).rowcount
            ob_cursor.close
            con.commit()
            con.close()

            return filas
        
        else:
            print("No se pudo establecer una conexion a la base de datos.")
            return -1
    except Error as error:
        print("Error al ejecutar SQL:" + str(error))
        return -1

def select(_sql, lista):
    try:
        con = conectar()
        if con:
            con.row_factory = diccionarios
            ob_cursor = con.cursor()

            if lista:
                ob_cursor.execute(_sql, lista)
            else:
                ob_cursor.execute(_sql)
            
            filas = ob_cursor.fetchall()
            ob_cursor.close
            con.close

            return filas
        else:
            print("No se pudo establecer una conexion")
            return None
    except Error as error:
        print("Error al ejecutar select" + str(error))
        return None

def diccionarios(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    
    return d