#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def par_impar(numero):
    if numero%2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

if __name__ == "__main__":

    numero = int(input("Introduce un número: "))

    print(par_impar(numero))

