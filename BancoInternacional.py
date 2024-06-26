import statistics
import math
import csv

"Lista de clientes y sus saldos"
datos_clientes = [
    {"cliente": "Mateo", "saldo": 350000},
    {"cliente": "Berta", "saldo": 800000},
    {"cliente": "Paula", "saldo": 600000},
    {"cliente": "Angelina", "saldo": 300000},
    {"cliente": "Michael", "saldo": 120000},
    {"cliente": "Fabian", "saldo": 500000},
    {"cliente": "Eduardo", "saldo": 550000},
    {"cliente": "Fabiola", "saldo": 720000},
    {"cliente": "Amalia", "saldo": 650000},
    {"cliente": "Magda", "saldo": 400000},
]

"Menu"
def menu():
    print(
        "Gestion Clientes Banco Internacional\n"
        "1. Mostrar saldos clasificados en rangos\n"
        "2. Saldo mas alto\n"
        "3. Saldo mas bajo\n"
        "4. Saldo promedio\n"
        "5. Media geometrica\n"
        "6. Reporte CSV\n"
        "7. Salir\n"
    )
    opcion = int(input("Ingrese una opcion: "))
    return opcion
