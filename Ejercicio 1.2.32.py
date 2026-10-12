def main():
    limite = int(input("Introduce el número límite: "))

    anterior = 0
    actual = 1

    while anterior <= limite:
        print(anterior)

        siguiente = anterior + actual
        anterior = actual
        actual = siguiente


if __name__ == "__main__":
    main()