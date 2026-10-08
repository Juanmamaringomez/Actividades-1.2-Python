def main():
    celsius = float(input("Introduce la temperatura en grados celsius: "))

    fahrenheit = (celsius * (9 / 5) + 32)

    print   (f"La temperatura en Fahrenheit es {fahrenheit} ºF")

if __name__ == "__main__":
    main()