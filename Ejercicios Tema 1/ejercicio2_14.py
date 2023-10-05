def peso_total(payaso,muñeca):
    return(112*payaso+75*muñeca)

if __name__ == "__main__":

    payaso = int(input("Introduce el número de payasos: "))
    muñeca = int(input("Introduce el número de muñeca: "))

    print("El peso total del envío es: " + str(peso_total(payaso,muñeca)) + "g.")