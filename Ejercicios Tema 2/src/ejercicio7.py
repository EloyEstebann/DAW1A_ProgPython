def renta(cantidad):
    if cantidad < 10000:
        return "Impositivo del 5%"
    elif 10000 <= cantidad < 20000:
        return "Impositivo del 15%"
    elif 20000 <= cantidad < 35000:
        return "Impositivo del 20%"
    elif 35000 <= cantidad < 60000:
        return "Impositivo del 30%"
    else:
        return "Impositivo del 45%"

if __name__ == "__main__":

    cantidad = int(input("Introduce la renta anual: "))
    print(renta(cantidad))