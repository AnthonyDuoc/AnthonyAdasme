import statistics
import math
import csv

#Lista de clientes y sus saldos correspondientes 
datos_clientes = [
    {"cliente": "Manuel Olivares", "saldo": 350000},
    {"cliente": "Berta Soto", "saldo": 800000},
    {"cliente": "Paula Correa", "saldo": 600000},
    {"cliente": "Angelina Castillo", "saldo": 200000},
    {"cliente": "Michael Adasme", "saldo": 120000},
    {"cliente": "Fabian Villalobos", "saldo": 500000},
    {"cliente": "Eduardo Gallardo", "saldo": 550000},
    {"cliente": "Christian Olivares", "saldo": 720000},
    {"cliente": "Elias Arana", "saldo": 650000},
    {"cliente": "Victor Adasme", "saldo": 400000},
]

#creacion de menu
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
    
#opcion 1 saldo clasificados en rangos

#creando tuplas para clasificar los saldos y rangos 
    def saldos_rangos():
        saldo_bajos = [(cliente["cliente"], cliente["saldo"]) for cliente in datos_clientes if cliente["saldo"] < 250000]
        saldo_medios = [(cliente["cliente"], cliente["saldo"]) for cliente in datos_clientes if cliente["saldo"] >= 250000 and cliente["saldo"] <= 500000]
        saldo_altos = [(cliente["cliente"], cliente["saldo"]) for cliente in datos_clientes if cliente["saldo"] > 500000]

#poniendo el orden de los saldos de menor a mayor
        saldo_bajos.sort(key = lambda x : x[1])
        saldo_medios.sort(key = lambda x : x[1])
        saldo_altos.sort(key = lambda x : x[1])

        print("Saldos en rangos: \n")
        print(f"Saldos bajos:")
        for cliente, saldo in saldo_bajos:
            formatted_saldo = f"{saldo:,}"
            print(f"- {cliente}: ${formatted_saldo}")

        print(f"\nSaldos medios:")
        for cliente, saldo in saldo_medios:
            formatted_saldo = f"{saldo:,}"
            print(f"- {cliente}: ${formatted_saldo}")

        print(f"\nSaldos altos:")
        for cliente, saldo in saldo_altos:
            formatted_saldo = f"{saldo:,}"
            print(f"- {cliente}: ${formatted_saldo}")

#opcion 2 saldo mas alto
    def saldo_mas_alto():
        for saldo_alto in datos_clientes:
                saldo_mas_alto = max(datos_clientes, key=lambda saldo_alto: saldo_alto["saldo"])
                if saldo_mas_alto["saldo"] == saldo_alto["saldo"]:
                    print("\nCliente con saldo mas alto: ")
                    print(f"- {saldo_mas_alto['cliente']}, Saldo Total: ${saldo_mas_alto['saldo']:,}\n")

#opcion 3 saldo mas bajo
    def saldo_mas_bajo():
        for saldo_bajo in datos_clientes:
                saldo_mas_bajo = min(datos_clientes, key=lambda saldo_bajo: saldo_bajo["saldo"])
                if saldo_mas_bajo["saldo"] == saldo_bajo["saldo"]:
                    print("\nCliente con saldo mas bajo: ")
                    print(f"- {saldo_mas_bajo['cliente']}, Saldo Total: ${saldo_mas_bajo['saldo']:,}\n")

#opcion 4 saldo promedio
    def saldo_promedio():
        saldo_p = [cliente["saldo"] for cliente in datos_clientes]
        saldo_promedio = statistics.mean(saldo_p)
        print(f"\nEl saldo promedio de los clientes es: ${saldo_promedio:,}")

#opcion 5 media geometrica
    def media_geometrica():
        saldo_g = [cliente["saldo"] for cliente in datos_clientes]
        log_saldo = sum(math.log(saldo) for saldo in saldo_g)
        saldo_geometrico = math.exp(log_saldo / len(saldo_g))
        print(f"\nLa media geometrica es: {saldo_geometrico:.2f}")

#opcion 6 reporte csv
    def reporte_csv():
        datos_clientes.sort(key=lambda cliente: cliente['saldo'], reverse=True)
        deduccion = float(10)
        deduccion /= 100
        with open("reporte_banco.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Saldo Neto($)" , "Saldo Deducido Imposicion($)"])
            for cliente in datos_clientes:
                formatted_saldo = f" ${cliente['saldo']:,} " 
                saldo_numerico = float(formatted_saldo.replace(",", "").replace("$", ""))
                saldo_deducido = saldo_numerico * (1 - deduccion)
                formatted_saldo_deducido = f" ${saldo_deducido:,.0f}"
                writer.writerow([cliente["cliente"], formatted_saldo,   formatted_saldo_deducido])
            print("\nEl reporte ha sido creado con exito.")

#opcion 7 salir del programa   
    def salir():
        print("Gracias por usar el programa")
        exit()

#definiendo las opciones del menu                           
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
            print("Gracias por usar nuestro servicio")
            exit()
        else:
            print("Opcion no valida")
            option = int(input("Ingrese una opcion: \n"))    

main()