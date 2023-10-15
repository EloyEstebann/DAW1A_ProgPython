def determinar_grupo(nombre,sexo):
    if(sexo == "M" and nombre[0].upper() < "M") or  (sexo == "H" and nombre[0].upper() > "N"):
        return "Tu grupo es el A"
    else:
        return "Tu grupo es el B"


if __name__ == "__main__":
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu sexo (H si eres hombre, M si eres mujer): ")
    print(determinar_grupo(nombre,sexo))
