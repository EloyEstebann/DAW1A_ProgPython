#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
#iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario 
#su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def tributar(sueldo,edad):
    if sueldo >= 1000 and edad>= 16:
        return "Puede tributar"
    else:
        return "No puede tributar"

if __name__ == "__main__":
    
    edad = int(input("Introduce tu edad: "))
    sueldo = int(input("Introduce tu sueldo: "))

    print(tributar(sueldo,edad))
