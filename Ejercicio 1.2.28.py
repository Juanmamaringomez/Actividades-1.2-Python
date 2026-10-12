import math


def main():
    a = float(input("Introduce el primer lado: "))
    b = float(input("Introduce el segundo lado: "))
    c = float(input("Introduce el tercer lado: "))

    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        print(f"El área del triángulo es: {area:.2f}")
    else:
        print("Las longitudes introducidas no pueden formar un triángulo.")


if __name__ == "__main__":
    main()