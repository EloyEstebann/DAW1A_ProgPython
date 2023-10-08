def iva_pagado(importe_final):
    return (importe_final*0.1)

def importe_siniva(importe_final,iva):
    return (importe_final-iva)


if __name__ == "__main__":
    importe_final = int(input("Introduce el importe final:"))
    iva = iva_pagado(importe_final)
    print("El IVA pagado es: " + str(iva_pagado(importe_final)))
    print("El importe sin IVA es: " + str(importe_siniva(importe_final,iva)))

