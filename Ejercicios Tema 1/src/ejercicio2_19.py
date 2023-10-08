def resultado_nombre_final(nombre):
    nombre = nombre.upper()
    nletras = len(nombre)
    return "Tu nombre es: " + nombre + " y tiene " + str(nletras) + " letras"

if __name__ == "__main__":

    nombre = input("Introduce tu nombre: ")
    print(resultado_nombre_final(nombre))

