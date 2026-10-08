def main ():
    horas = float(input("Introduce las horas de trabajo: "))
    precio_hora = float (input("Introduce el precio por hora: "))

    total_precio = horas * precio_hora 

    print(f"El importe total por los servicios es {total_precio} €")

if __name__ == "__main__":
    main()  