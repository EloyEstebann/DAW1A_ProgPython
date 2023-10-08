INTERES = 0.4

def cantidad_final(dinerodep):
    for n in range(3):
        dinerodep += dinerodep * INTERES
        print("La cantidad del año " + str(n+1) + " es " + str(round(dinerodep,2)))
    return dinerodep

if __name__ == "__main__":

    dinerodep = int(input("Indica el importe depositado: "))
    print("La cantidad total en 3 años es " + str(round(cantidad_final(dinerodep),2)))
