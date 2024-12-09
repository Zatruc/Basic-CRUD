from database import conectar_db


def menu_citas():
    print("--- MENU CITAS ---")
    while True:
        print("1. Agregar Cita")
        print("2. Consultar Citas")
        print("3. Modificar Cita")
        print("4. Eliminar Cita")
        print("5. Salir")

        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            agregar_cita()
        if opcion == 2:
            consultar_citas()
        if opcion == 3:
            modificar_cita()
        if opcion == 4:
            eliminar_cita()
        if opcion == 5:
            break


def agregar_cita():
    paciente_id = input("Ingrese el ID del paciente: ")
    doctor_id = input("Ingrese el ID del doctor: ")
    fecha_hora = input("Ingrese la fecha y hora de la cita (YYYY-MM-DD HH:MM:SS): ")
    motivo = input("Ingrese el motivo de la cita: ")

    conexion = conectar_db()
    cursor = conexion.cursor()

    sql_insert = "INSERT INTO Citas (Paciente_ID, Doctor_ID, Fecha_Hora, Motivo) VALUES (?, ?, ?, ?)"
    values = (paciente_id, doctor_id, fecha_hora, motivo)

    cursor.execute(sql_insert, values)
    conexion.commit()
    conexion.close()
    print("Cita agregada con exito.")


def consultar_citas():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
    SELECT Citas.ID, Pacientes.Nombre, Pacientes.Apellido, Doctores.Nombre, Doctores.Apellido, Citas.Fecha_Hora, Citas.Motivo
    FROM Citas
    INNER JOIN Pacientes ON Citas.Paciente_ID = Pacientes.ID
    INNER JOIN Doctores ON Citas.Doctor_ID = Doctores.ID
    """
    )
    # esta forma de consulta esta mal, solo recupera la primera cita (CORREGIR)
    # CORREGIR TODOEL APARTADO DE CITAS EN GENERAL

    resultados = cursor.fetchall()

    print("\n--- Lista de Citas ---")
    for cita in resultados:
        print(
            f"Cita ID: {cita[0]}, Paciente: {cita[1]} {cita[2]}, Doctor: {cita[3]} {cita[4]}, Fecha y Hora: {cita[5]}, Motivo: {cita[6]}"
        )

    conexion.close()


def modificar_cita():
    consultar_citas()
    id_cita = input("Ingrese el ID de la cita a modificar: ")

    fecha_hora = input(
        "Ingrese la nueva fecha y hora (YYYY-MM-DD HH:MM:SS) (dejar en blanco si no desea cambiar): "
    )
    motivo = input(
        "Ingrese el nuevo motivo de la cita (dejar en blanco si no desea cambiar): "
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Citas WHERE ID = ?", (id_cita))
    cita = cursor.fetchone()

    fecha_hora = fecha_hora if fecha_hora else cita[3]
    motivo = motivo if motivo else cita[4]

    sql_update = "UPDATE Citas SET Fecha_Hora = ?, Motivo = ? WHERE ID = ?"
    values = (fecha_hora, motivo, id_cita)

    cursor.execute(sql_update, values)
    conexion.commit()
    conexion.close()
    print("Cita modificada con exito.")


def eliminar_cita():
    consultar_citas()
    id_cita = input("Ingrese El ID de la cita a eliminar: ")

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Citas WHERE ID = ?", (id_cita))
    conexion.commit()
    conexion.close()
    print("Cita eliminada con exito.")
