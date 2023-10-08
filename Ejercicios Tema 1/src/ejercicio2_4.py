def calculo(celsius):
    return((celsius*9/5)+32)

if __name__ == "__main__":
    celsius = int(input("Introduce la temperatura en celsius: "))
    print("La temperatura en farenheit es: " + str(calculo(celsius)))