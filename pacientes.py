from database import conectar_db


def menu_pacientes():
    print("--- MENU PRINCIPAL ---")
    while True:
        print("1. Agregar Paciente")
        print("2. Consultar Paciente")
        print("3. Modificar Paciente")
        print("4. Eliminar Paciente")
        print("5. Salir")

        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            agregar_paciente()
        if opcion == 2:
            consultar_pacientes()
        if opcion == 3:
            modificar_pacientes()
        if opcion == 4:
            eliminar_paciente()
        if opcion == 5:
            break


def agregar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    telefono = input("Ingrese el telefono del paciente: ")
    direccion = input("Ingrese la direccion del paciente: ")
    correo = input("Ingrese el correo electronico del paciente: ")

    conexion = conectar_db()
    cursor = conexion.cursor()

    sql_insert = "INSERT INTO Pacientes (Nombre, Apellido, Fecha_de_Nacimiento, Telefono, Direccion, Correo_Electronico) VALUES (?, ?, ?, ?, ?, ?)"
    values = (nombre, apellido, fecha_nacimiento, telefono, direccion, correo)

    cursor.execute(sql_insert, values)
    conexion.commit()
    conexion.close()
    print("Paciente agregado con exito.")


def consultar_pacientes():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Pacientes")
    resultados = cursor.fetchall()

    print("\n--- Lista de Pacientes ---")
    for paciente in resultados:
        print(
            f"ID: {paciente[0]}, Nombre: {paciente[1]}, Apellido: {paciente[2]}, Fecha de Nacimiento: {paciente[3]}, Telefono: {paciente[4]}, Direccion: {paciente[5]}, Correo: {paciente[6]}"
        )

    conexion.close()


def modificar_pacientes():
    consultar_pacientes()
    id_paciente = input("Ingrese el ID del paciente a modificar: ")

    nombre = input(
        "Ingrese el nuevo nombre del paciente (dejar en blanco si no desea cambiar): "
    )
    apellido = input(
        "Ingrese el nuevo apellido del paciente (dejar en blanco si no desea cambiar): "
    )
    fecha_nacimiento = input(
        "Ingrese la nueva fecha de nacimiento (YYYY-MM-DD) (dejar en blanco si no desea cambiar): "
    )
    telefono = input(
        "Ingrese el nuevo telefono del paciente (dejar en blanco si no desea cambiar): "
    )
    direccion = input(
        "Ingrese la nueva direccion del paciente (dejar en blanco si no desea cambiar): "
    )
    correo = input(
        "Ingrese el nuevo correo electronico del paciente (dejar en blanco si no desea cambiar): "
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Pacientes WHERE ID = ?", (id_paciente))
    paciente = cursor.fetchone()

    nombre = nombre if nombre else paciente[1]
    apellido = apellido if apellido else paciente[2]
    fecha_nacimiento = fecha_nacimiento if fecha_nacimiento else paciente[3]
    telefono = telefono if telefono else paciente[4]
    direccion = direccion if direccion else paciente[5]
    correo = correo if correo else paciente[6]

    slq_update = "UPDATE Pacientes SET Nombre = ?, Apellido = ?, Fecha_de_Nacimiento = ?, Telefono = ?, Direccion = ?, Correo_Electronico = ? WHERE ID = ?"
    values = (
        nombre,
        apellido,
        fecha_nacimiento,
        telefono,
        direccion,
        correo,
        id_paciente,
    )

    cursor.execute(slq_update, values)
    conexion.commit()
    cursor.close()
    print("Paciente modificado con exito.")


def eliminar_paciente():
    consultar_pacientes()
    id_paciente = input("Ingrese El ID del paciente a eliminar: ")

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Pacientes WHERE ID = ?", (id_paciente))
    conexion.commit()
    cursor.close()
    print("Paciente eliminado con exito.")
