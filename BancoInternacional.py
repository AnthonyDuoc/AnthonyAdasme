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
            "\nGestion Clientes Banco Internacional :\n"
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
        saldo_bajos = [(cliente["cliente"], cliente["saldo"]) for cliente in datos_clientes if cliente["saldo"] < 250000]
        saldo_medios = [(cliente["cliente"], cliente["saldo"]) for cliente in datos_clientes if cliente["saldo"] >= 250000 and cliente["saldo"] <= 500000]
        saldo_altos = [(cliente["cliente"], cliente["saldo"]) for cliente in datos_clientes if cliente["saldo"] > 500000]

        saldo_bajos.sort(key = lambda x : x[1])
        saldo_medios.sort(key = lambda x : x[1])
        saldo_altos.sort(key = lambda x : x[1])

        print("Saldos en rangos: \n")
        print(f"Saldos bajos:")
        for cliente, saldo in saldo_bajos:
            print(f"- {cliente}: {saldo}")

        print(f"\nSaldos medios:")
        for cliente, saldo in saldo_medios:
            print(f"- {cliente}: {saldo}")

        print(f"\nSaldos altos:")
        for cliente, saldo in saldo_altos:
            print(f"- {cliente}: {saldo}")

        
    def saldo_mas_alto():
        for saldo_alto in datos_clientes:
                saldo_mas_alto = max(datos_clientes, key=lambda saldo_alto: saldo_alto["saldo"])
                if saldo_mas_alto["saldo"] == saldo_alto["saldo"]:
                    print("\nCliente con saldo mas alto : ")
                    print(f"- {saldo_mas_alto['cliente']}, Saldo Total : {saldo_mas_alto['saldo']}$\n")

    def saldo_mas_bajo():
        for saldo_bajo in datos_clientes:
                saldo_mas_bajo = min(datos_clientes, key=lambda saldo_bajo: saldo_bajo["saldo"])
                if saldo_mas_bajo["saldo"] == saldo_bajo["saldo"]:
                    print("\nCliente con saldo mas bajo : ")
                    print(f"- {saldo_mas_bajo['cliente']}, Saldo Total : {saldo_mas_bajo['saldo']}$\n")

    def saldo_promedio():
        saldo_p = [cliente["saldo"] for cliente in datos_clientes]
        saldo_promedio = statistics.mean(saldo_p)
        print(f"\nEl saldo promedio es: {saldo_promedio}$")
    
    def media_geometrica():
        saldo_g = [cliente["saldo"] for cliente in datos_clientes]
        saldo_geometrico = statistics.geometric_mean(saldo_g)
        print(f"La media geometrica es: {saldo_geometrico}")

    def reporte_csv():
        with open("reporte_banco.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Saldo"])
            for cliente in datos_clientes:
                writer.writerow([cliente["cliente"], cliente["saldo"]])
        print("El reporte ha sido creado con exito")
    
    def salir():
        print("Gracias por usar el programa")
        exit()
                            
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
            exit()
        else:
            print("Opcion no valida")
            option = int(input("Ingrese una opcion: \n"))    

main()