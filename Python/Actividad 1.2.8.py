def main():

    numero = float(input("Introduce el primer número: "))
    suma = numero
    numero = float(input("Introduce el segundo número: "))
    suma = suma + numero
    numero = float(input("Introduce el tercer número: "))
    suma = suma + numero

    print(f"La suma de los tres números es: {suma}")

if __name__ == "__main__":
    main()  