def nivel(puntuacion):
    if 0.0 <= puntuacion < 0.4:
        return "Su nivel es inaceptable, su dinero es 2400"
    elif 0.4 <= puntuacion < 0.6:
        return "Su nivel es aceptable, su dinero es 3360"
    else:
        return "Su nivel es meritorio, su dinero es 3840"

if __name__ == "__main__":

    puntuacion = float(input("Introduce tu puntuacion en formato 0.n: "))
    print(nivel(puntuacion))