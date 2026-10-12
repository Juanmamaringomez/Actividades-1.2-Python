def main():
    ahorro = float(input("Introduce la cantidad de dinero depositada: "))

    ahorro = ahorro * 1.04
    print(f"Después del primer año: {ahorro:.2f} €")

    ahorro = ahorro * 1.04
    print(f"Después del segundo año: {ahorro:.2f} €")

    ahorro = ahorro * 1.04
    print(f"Después del tercer año: {ahorro:.2f} €")


if __name__ == "__main__":
    main()