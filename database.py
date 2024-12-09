import sqlite3

ruta_db = r"C:\Users\USER\Documents\3-Periodo\Bases de Datos Relacionales\3-Parcial\Repaso-BDD\Citas-Repaso.db"


def conectar_db():
    return sqlite3.connect(ruta_db)


def crear_tablas():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Pacientes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            Fecha_de_Nacimiento DATE,
            Telefono TEXT,
            Direccion TEXT,
            Correo_Electronico TEXT
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Doctores (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            Especialidad TEXT NOT NULL,
            Telefono TEXT,
            Correo_Electronico TEXT
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Citas (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Paciente_ID INTEGER,  -- Relación con la tabla Pacientes
            Doctor_ID INTEGER, -- Relacion con la tabla Doctores
            Fecha_Hora DATETIME NOT NULL,
            Motivo TEXT,
            FOREIGN KEY (Paciente_ID) REFERENCES Pacientes(ID)
            FOREIGN KEY (Doctor_ID) REFERENCES Doctores(ID)
        );
        """
    )

    conexion.commit
    cursor.close()
