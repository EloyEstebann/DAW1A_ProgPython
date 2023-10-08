def cociente(m,n):
    return(m//n)

def resto(m,n):
    return(m%n)

if __name__ == "__main__":

    m = int(input("Introduce el dividendo: "))
    n = int(input("Introduce el divisor: "))

    print("El cociente es: " + str(cociente(m,n)))

    print("El resto es: " + str(resto(m,n)))