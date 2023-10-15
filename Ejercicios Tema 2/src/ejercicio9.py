def entrada(edad):
    if edad < 4:
        return "Entrada gratis!!"
    elif 4 <= edad < 18:
        return "Entrada 5 euros!!"
    else:
        return "Entrada 10 euros!!"


if __name__ == "__main__":
    
    edad = int(input("Introduce tu edad pa ver el precio de la entrada: "))
    print(entrada(edad))