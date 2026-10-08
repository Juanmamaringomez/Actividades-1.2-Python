def main():
    importe = float(input("Introduce el importe sin IVA: "))
    iva = float(input("Introduce el IVA (%): "))

    precio_final = importe + (importe * iva/100)

    print(f"El precio final del articulo es: {precio_final} €")

if __name__ == "__main__":
    main()