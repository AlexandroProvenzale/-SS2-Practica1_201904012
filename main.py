import pandas as pd
import pyodbc as sql
import os
from os import system
from dotenv import load_dotenv

load_dotenv()

credentials = {
    'server': os.getenv('DATABASE_SERVER'),
    'database': os.getenv('DATABASE_NAME')
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
    for statement in reader.split(';'):
        if len(statement) > 1:
            cursor.execute(statement)
            response = cursor.fetchall()
            print(response)

    
def main():
    options = ["1. Borrar modelo", "2. Crear modelo", "3. Extraer informacion", "4. Cargar informacion", "5. Realizar consultas", "6. Salir"]
    while True:
        conn = newConnection()
        print()
        for option in options:
            print( option)

        chooseOpt()

        if opt == 1:
            continue
        elif opt == 6:
            print("\nHasta la vista")
            break


if __name__ == '__main__':
    main()