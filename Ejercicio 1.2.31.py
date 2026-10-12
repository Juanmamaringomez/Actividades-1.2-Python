def main():
    numero = int(input("Introduce un número entero positivo: "))

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            print(divisor)


if __name__ == "__main__":
    main()