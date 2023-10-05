def indicecorporal(peso,estatura):
    return(peso/(estatura*estatura))


if __name__ == "__main__":

    peso = float(input("Introduce el peso: "))
    estatura = float(input("Introduce la estatura: "))

    print("Su indice de masa corporal es: " + str(round(indicecorporal(peso,estatura),2)))