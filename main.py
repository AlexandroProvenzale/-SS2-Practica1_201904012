import pyodbc as sql
import os
from os import system
from dotenv import load_dotenv

load_dotenv()

credentials = {
    'server': os.getenv('DATABASE_SERVER'),
    'database': os.getenv('DATABASE_NAME')
}

rootPath = "D:\\PythonProjects\\Semi_Practica1\\Scripts\\"

sqlPaths = {
    'borrarModelo': rootPath + "BorrarModelo.sql",
    'crearModelo': rootPath + "CrearModelo.sql",
    'cargarInformacion': rootPath + "CargarInformacion.sql",
    'realizarConsultas': rootPath + "RealizarConsultas.sql"
}

def newConnection():
    try:
        connection = sql.connect(
            'DRIVER={ODBC Driver 17 for SQL server};SERVER=' + credentials['server'] + ';DATABASE=' + credentials[
                'database'] + ';Trusted_Connection=yes;'
        )
        print('Conectado a la base de datos')
        return connection
    except sql.Error as error:
        print(error)

def chooseOpt():
    global opt
    while True:
        try:
            opt  = int(input("\nElige una opción: "))
        except ValueError:
            print("\nPor favor, ingresa un número entero")
            continue
        else:
            print(f'\nElegiste la opción {opt}')
            break

def exec(conn, path):
    file = open(path)
    reader = file.read()
    cursor = conn.cursor()
    try:
        for statement in reader.split(';'):
            if len(statement) > 2:
                cursor.execute(statement)
    except sql.Error as error:
        print("\n" + error)
    return cursor

    
def main():
    global opt
    conn = newConnection()
    while True:
        print('''
        1. Borrar modelo
        2. Crear modelo
        3. Extraer informacion
        4. Cargar informacion
        5. Realizar consultas
        6. Salir
        ''')

        chooseOpt()

        if opt == 1:
            _ = exec(conn, sqlPaths['borrarModelo'])
        elif opt == 2:
            _ = exec(conn, sqlPaths['crearModelo'])
        elif opt == 3:
            continue
        elif opt == 4:
            _ = exec(conn, sqlPaths['cargarInformacion'])
        elif opt == 5:
            cursor = exec(conn, sqlPaths['realizarConsultas'])
            response = cursor.fetchall()
            print(response)
        elif opt == 6:
            print("\nHasta la vista")
            break
        else:
            print("\nIngresar opción válida")


if __name__ == '__main__':
    main()