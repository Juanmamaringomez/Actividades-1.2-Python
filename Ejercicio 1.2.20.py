def main():
    telefono = input("Introduce el número de teléfono (+34-número-extensión): ")

    numero = telefono[4:-3]

    print(f"El número de teléfono es: {numero}")


if __name__ == "__main__":
    main()