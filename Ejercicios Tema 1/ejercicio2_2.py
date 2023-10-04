def importe_total(horas,precio):
    return(horas*precio)

if __name__=="__main__":
    horas = int(input("Horas de trabajo: "))
    precio = int(input("Coste por hora: "))

    print("Importe total: " + str(importe_total(horas,precio)))