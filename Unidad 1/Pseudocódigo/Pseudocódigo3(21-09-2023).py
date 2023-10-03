def main():
    # Lee 3 números del usuario
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))

    # Crea una lista con los números y ordena la lista
    numeros = [num1, num2, num3]
    numeros.sort()

    # Imprime los números ordenados
    print("Los números ordenados de menor a mayor son:")
    for num in numeros:
        print(num)

if __name__ == "__main__":
    main()
