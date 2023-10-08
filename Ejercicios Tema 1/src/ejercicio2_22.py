def transformacion(frase, vocal):
    vocal_minuscula = vocal.lower()
    vocal_mayuscula = vocal.upper()
    nueva_frase = frase.replace(vocal_minuscula, vocal_mayuscula)
    return nueva_frase


if __name__ == "__main__":
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una única vocal: ")
    print(transformacion(frase,vocal))