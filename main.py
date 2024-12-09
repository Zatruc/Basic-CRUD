from database import crear_tablas
from pacientes import *
from doctores import *
from citas import *


def menu_principal():
    crear_tablas()
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1. Pacientes")
        print("2. Doctores")
        print("3. Citas")
        print("4. Salir")

        opcion = int(input("A que menu quieres ingresar? "))
        if opcion == 1:
            menu_pacientes()
        elif opcion == 2:
            menu_doctores()
        elif opcion == 3:
            menu_citas()
        elif opcion == 4:
            break


if __name__ == "__main__":
    menu_principal()
