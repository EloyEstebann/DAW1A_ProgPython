def comprobacion(guardada,usuario):
    if guardada == usuario:
        return "La contraseña es correcta"
    else:
        return "La contraseña no es correcta"

if __name__ == "__main__":
    
    guardada = "contraseña"
    usuario = input("Introduce la contraseña: ")

    print(comprobacion(guardada,usuario))