import csv
import os


def menu():
    print('1. Guardar datos empleados')
    print('2. Leer Datos empleados ')
    print('0. Salir')

def menu_secundario():
    print('1. ¿Quiere Continuar Cargando Datos en CSV?')
    print('0. Salir')

def legajos_empleados():
    empleados = 'empleados.csv'
    vacaciones = 'dias.csv'
    while True:
        while True:
            try:
                menu()
                option = int(input('Ingresar una opción:'))
                if 0 <= option <= 2:
                    break
                else:
                    print('Ingresar un valor mayor o igual cero.')
            except ValueError:
                print('Error: Ingresar un valor entero')
        if option == 0:
            break
        elif option == 1:
            if os.path.exists('empleados.csv'):
                pregunta = input('1:quiere modificar el archivo o 2: sobreescribirlo')
                if pregunta == 1:
                    ARCHIVO = pregunta == 'a'
                    carga_empleados(empleados, ARCHIVO)
                elif pregunta == 2:
                    ARCHIVO = pregunta == 'w'
                    carga_empleados(empleados, ARCHIVO)

        elif option == 2:
            vacaciones_fechas(empleados, vacaciones)

def carga_empleados(empleados, ARCHIVO):

    datos = True
    while datos:
        lista_empleados = []
        empleado = []
        fields = ['Legajo', 'Apellido', 'Nombre', 'Año', 'Total Vacaciones']

        for campo in fields:
            empleado.append(input(f"Ingrese {campo} del empleado: "))

        lista_empleados.append(empleado)
        try:
            with open(empleados, ARCHIVO, newline='') as file:
                file_guarda = csv.writer(file)
                file_guarda.writerows(lista_empleados)
                return
        except IOError:
            print("Ocurrio un error con el archivo")


def vacaciones_fechas(empleados,vacaciones):

    try:
        vacaciones_leg = open(vacaciones)
        empleados_leg = open(empleados)
        vacaciones_csv = csv.reader(vacaciones_leg)
        empleados_csv = csv.reader(empleados_leg)
    except IOError:
        (print("Error"))

legajos_empleados()
