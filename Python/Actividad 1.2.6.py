def main():
    importe_final = float(input("Introduce el importe final: "))

    importe_sin_iva = importe_final / 1.10
    iva_pagado = importe_final - importe_sin_iva

    print (f"El importe sin IVA es: {importe_sin_iva} €")
    print (f"El IVA pagado es: {iva_pagado} €")


if __name__ == "__main__":
    main()