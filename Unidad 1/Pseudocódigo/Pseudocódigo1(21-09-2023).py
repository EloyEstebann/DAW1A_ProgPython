def solicitar_numero():
    while True:
        try:
            numero = int(input("Introduce un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                return numero
            else:
                print("El número no está en el rango de 1 a 10. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Uso de la función
num = solicitar_numero()
print(f"Has introducido el número {num} que es correcto")
