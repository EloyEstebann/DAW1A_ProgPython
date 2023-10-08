def resultado_nombre(nombrecompleto):
    nombre_minusculas = nombrecompleto.lower()
    nombre_mayusculas = nombrecompleto.upper()
    separar_palabra = nombrecompleto.split()
    nombre_final = ''.join([palabra.capitalize() for palabra in separar_palabra])

    return nombre_minusculas, nombre_mayusculas, nombre_final

if __name__ == "__main__":

    nombrecompleto = input("Escribe tu nombre completo: ")

    nombre_minusculas, nombre_mayusculas, nombre_final = resultado_nombre(nombrecompleto)

    print(str(nombre_minusculas))
    print(str(nombre_mayusculas))
    print(str(nombre_final))

