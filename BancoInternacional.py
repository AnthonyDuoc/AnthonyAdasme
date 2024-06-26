import statistics
import math
import csv

"Lista de clientes y sus saldos"
datos_clientes = [
    {"cliente": "Mateo", "saldo": 350000},
    {"cliente": "Berta", "saldo": 800000},
    {"cliente": "Paula", "saldo": 600000},
    {"cliente": "Angelina", "saldo": 200000},
    {"cliente": "Michael", "saldo": 120000},
    {"cliente": "Fabian", "saldo": 500000},
    {"cliente": "Eduardo", "saldo": 550000},
    {"cliente": "Fabiola", "saldo": 720000},
    {"cliente": "Amalia", "saldo": 650000},
    {"cliente": "Magda", "saldo": 400000},
]

"Menu"
def main():
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
        option = int(input("Ingrese una opcion: "))

      

        def saldos_rangos():
            print("Saldos clasificados en rangos\n")
            for cliente in datos_clientes:
                saldo = cliente["saldo"]
                if saldo <= 250000:
                    print("Clientes con saldo menor o igual a 250.000: ")
                    print(f"{cliente['cliente']} tiene un saldo de {saldo}")
                if saldo > 250000 and saldo <= 500000: 
                    print("Clientes con saldo entre 250.000 y 500.000: ")
                    print(f"{cliente['cliente']} tiene un saldo de {saldo}")
                else:
                    print("Clientes con saldo mayor a 500.000: ")
                    print(f"{cliente['cliente']} tiene un saldo de {saldo}")
                
        while True:
            if option == 1:
                saldos_rangos()
            elif option == 2:
                saldo_mas_alto()
            elif option == 3:
                saldo_mas_bajo()
            elif option == 4:
                saldo_promedio()
            elif option == 5:
                media_geometrica()
            elif option == 6:
                reporte_csv()
            elif option == 7:
                break
            else:
                print("Opcion no valida")
                option = int(input("Ingrese una opcion: "))    









main()