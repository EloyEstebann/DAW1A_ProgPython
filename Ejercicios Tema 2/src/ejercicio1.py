def funcionedad(edad):
    if edad >= 18:
        return "Soy mayor de edad!!"
    
    else: 
        return "Soy menor de edad!!"

if __name__ == "__main__":
    edad = int(input("Introduce tu edad: "))

    print(funcionedad(edad))