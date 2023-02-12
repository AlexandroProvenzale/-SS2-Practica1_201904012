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


def execScript(conn, path, select):
    global cntr
    cntr = 0
    file = open(path)
    reader = file.read()
    cursor = conn.cursor()
    try:
        for statement in reader.split(';'):
            if len(statement) > 2:
                cursor.execute(statement)
                if select:
                    cntr += 1
                    rows = cursor.fetchall()
                    if cntr != 10: #Cambiar a 3 por favooooooooooor
                        string = ""
                        print("\nConsulta " + str(cntr) + "\n")
                        header = False
                        for row in rows:
                            if not header:
                                string += ", ".join(t[0] for t in row.cursor_description) + "\n"
                                print("| ", " | ".join(t[0] for t in row.cursor_description), " |")
                                header = True
                            print("| ", " | ".join(str(item) for item in row), " |")
                            string += ", ".join(str(item) for item in row) + "\n"
                        f = open("Consulta" + str(cntr) + ".csv", "w")
                        f.write(string)
                        f.close()
                    else:
                        continue
        conn.commit()
    except sql.Error as error:
        print("\n" + error)


def main():
    global opt
    conn = newConnection()
    while True:
        print("""
        1. Borrar modelo
        2. Crear modelo
        3. Extraer informacion
        4. Cargar informacion
        5. Realizar consultas
        6. Salir
        """
        )

        chooseOpt()

        if opt == 1:
            execScript(conn, sqlPaths['borrarModelo'], False)
            print("\nSe borró el modelo correctamente")
        elif opt == 2:
            execScript(conn, sqlPaths['crearModelo'], False)
            print("\nSe creó el modelo correctamente")
        elif opt == 3:
            continue
        elif opt == 4:
            execScript(conn, sqlPaths['cargarInformacion'], False)
            print("\nSe Cargó la información al modelo correctamente")
        elif opt == 5:
            execScript(conn, sqlPaths['realizarConsultas'], True)
        elif opt == 6:
            print("\nHasta la vista")
            break
        else:
            print("\nIngresar opción válida")


if __name__ == '__main__':
    main()