import statistics
import math
import csv
import os

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
        return option
      

    def saldos_rangos():
        print("Saldos clasificados en rangos\n")
        for rango in datos_clientes:
            saldo = rango["saldo"]
            if saldo <= 250000:
                print("Clientes con saldo menor o igual a 250.000: ")
                print(f"{rango['cliente']} tiene un saldo de {saldo}")
            if saldo > 250000 and saldo <= 500000: 
                print("Clientes con saldo entre 250.000 y 500.000: ")
                print(f"{rango['cliente']} tiene un saldo de {saldo}")
            else:
                print("Clientes con saldo mayor a 500.000: ")
                print(f"{rango['cliente']} tiene un saldo de {saldo}")

    def saldo_mas_alto():
        for saldo_alto in datos_clientes:
                saldo_mas_alto = max(datos_clientes, key=lambda saldo_alto: saldo_alto["saldo"])
                if saldo_mas_alto["saldo"] == saldo_alto["saldo"]:
                    print(f"El cliente con el saldo mas alto es {saldo_mas_alto['cliente']}, Saldo Total :{saldo_mas_alto['saldo']}$")

    def saldo_mas_bajo():
        for saldo_bajo in datos_clientes:
                saldo_mas_bajo = min(datos_clientes, key=lambda saldo_bajo: saldo_bajo["saldo"])
                if saldo_mas_bajo["saldo"] == saldo_bajo["saldo"]:
                    print(f"El cliente con el saldo mas bajo es {saldo_mas_bajo['cliente']}, Saldo Total : {saldo_mas_bajo['saldo']}$")

    def saldo_promedio():
        saldo_p = [cliente["saldo"] for cliente in datos_clientes]
        saldo_promedio = statistics.mean(saldo_p)
        print(f"El saldo promedio es: {saldo_promedio}")
    
    def media_geometrica():
        saldo_g = [cliente["saldo"] for cliente in datos_clientes]
        saldo_geometrico = statistics.geometric_mean(saldo_g)
        print(f"La media geometrica es: {saldo_geometrico}")
                            
    while True:
        option = menu()
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
            print("Gracias por usar el programa")
        else:
            print("Opcion no valida")
            option = int(input("Ingrese una opcion: "))    









main()