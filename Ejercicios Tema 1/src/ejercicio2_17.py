def bucle(nombre, n):
    resultado = ""
    
    for contador in range(n):
        resultado += nombre + "\n"
    return resultado 

if __name__ == "__main__":

    nombre = input("Escriba su nombre: ")
    n = int(input("Escriba un número entero: "))
    
    
   
    print(bucle(nombre, n))