def main():
    PRECIO_BARRA = 3.49
    DESCUENTO = 0.60

    barras = int(input("Introduce el número de barras no frescas vendidas: "))

    descuento = PRECIO_BARRA * DESCUENTO
    precio_final = PRECIO_BARRA - descuento
    coste_total = barras * precio_final

    print(f"Precio habitual de una barra: {PRECIO_BARRA:.2f} €")
    print(f"Descuento aplicado: {DESCUENTO * 100:.0f}%")
    print(f"Coste total de las barras no frescas: {coste_total:.2f} €")


if __name__ == "__main__":
    main()