def main():
    n = int(input("Introduce el primer número entero: "))
    m = int(input("Introduce el segundo número entero: "))

    if m == 0:
        print("No se puede dividir entre cero.")
    else:
        c = n // m
        r = n % m

        print(f"La división de {n} entre {m} da un cociente {c} y un resto {r}")


if __name__ == "__main__":
    main()
