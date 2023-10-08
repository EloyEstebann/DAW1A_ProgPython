def numerotelefono(numero):
    partes = numero.split('-')
    return partes[1]

if __name__ == "__main__":
    numero = input("Introduce un número con formato 34-xxxxxxxxx: ")
    print(numerotelefono(numero))