from database import conectar_db


def menu_doctores():
    print("--- MENU DOCTORES ---")
    while True:
        print("1. Agregar Doctor")
        print("2. Consultar Doctores")
        print("3. Modificar Doctor")
        print("4. Eliminar Doctor")
        print("5. Salir")

        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            agregar_doctor()
        if opcion == 2:
            consultar_doctores()
        if opcion == 3:
            modificar_doctor()
        if opcion == 4:
            eliminar_doctor()
        if opcion == 5:
            break


def agregar_doctor():
    nombre = input("Ingrese el nombre del doctor: ")
    apellido = input("Ingrese el apellido del doctor: ")
    especialidad = input("Ingrese la especialidad del doctor: ")
    telefono = input("Ingrese el telefono del doctor: ")
    correo = input("Ingrese el correo electronico del doctor: ")

    conexion = conectar_db()
    cursor = conexion.cursor()

    sql_insert = "INSERT INTO Doctores (Nombre, Apellido, Especialidad, Telefono, Correo_Electronico) VALUES (?, ?, ?, ?, ?)"
    values = (nombre, apellido, especialidad, telefono, correo)

    cursor.execute(sql_insert, values)
    conexion.commit()
    conexion.close()
    print("Doctor agregado con exito.")


def consultar_doctores():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
    SELECT Doctores.ID, Doctores.Nombre, Doctores.Apellido, Doctores.Especialidad, Doctores.Telefono, Doctores.Correo_Electronico, COUNT(Citas.ID) AS Citas_Asignadas
    FROM Doctores
    LEFT JOIN Citas ON Doctores.ID = Citas.Doctor_ID
    GROUP BY Doctores.ID
    """
    )

    resultados = cursor.fetchall()

    print("\n--- Lista de Doctores ---")
    for doctor in resultados:
        citas_info = (
            "Tiene citas asignadas." if doctor[6] > 0 else "No tiene citas asignadas."
        )
        print(
            f"ID: {doctor[0]}, Nombre: {doctor[1]} {doctor[2]}, Especialidad: {doctor[3]}, Teléfono: {doctor[4]}, Correo: {doctor[5]}, {citas_info}"
        )

    conexion.close()


def modificar_doctor():
    consultar_doctores()
    id_doctor = input("Ingrese el ID del doctor a modificar: ")

    nombre = input(
        "Ingrese el nuevo nombre del doctor (dejar en blanco si no desea cambiar): "
    )
    apellido = input(
        "Ingrese el nuevo apellido del doctor (dejar en blanco si no desea cambiar): "
    )
    especialidad = input(
        "Ingrese la nueva especialidad del doctor (dejar en blanco si no desea cambiar): "
    )
    telefono = input(
        "Ingrese el nuevo telefono del doctor (dejar en blanco si no desea cambiar): "
    )
    correo = input(
        "Ingrese el nuevo correo electronico del doctor (dejar en blanco si no desea cambiar): "
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Doctores WHERE ID = ?", (id_doctor))
    doctor = cursor.fetchone()

    nombre = nombre if nombre else doctor[1]
    apellido = apellido if apellido else doctor[2]
    especialidad = especialidad if especialidad else doctor[3]
    telefono = telefono if telefono else doctor[4]
    correo = correo if correo else doctor[5]

    sql_update = "UPDATE Doctores SET Nombre = ?, Apellido = ?, Especialidad = ?, Telefono = ?, Correo_Electronico = ? WHERE ID = ?"
    values = (nombre, apellido, especialidad, telefono, correo, id_doctor)

    cursor.execute(sql_update, values)
    conexion.commit()
    conexion.close()
    print("Doctor modificado con exito.")


def eliminar_doctor():
    consultar_doctores()
    id_doctor = input("Ingrese El ID del doctor a eliminar: ")

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Doctores WHERE ID = ?", (id_doctor))
    conexion.commit()
    conexion.close()
    print("Doctor eliminado con exito.")
