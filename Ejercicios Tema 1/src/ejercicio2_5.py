def importe_final1(precio_sin_iva,iva1):
    return precio_sin_iva + iva1

def importe_final2(precio_sin_iva,iva2):
   return  precio_sin_iva + iva2

def importe_final3(precio_sin_iva,iva3):
    return precio_sin_iva + iva3

if __name__ == "__main__":
    precio_sin_iva = float(input("Introduzca el importe sin iva: "))
   
    
    print("Opcion 1: IVA al 21%\n")
    print("Opcion 2: IVA al 10%\n")
    print("Opcion 3: IVA al 4%\n")
    seleccion = int(input("Seleccione el tipo de iva: "))
    
    iva1 = 0.21
    iva2 = 0.10
    iva3 = 0.04


    if seleccion == 1:
        iva = precio_sin_iva * 21/100
        print("El precio total es: " + str(importe_final1(precio_sin_iva,iva)))
    
    elif seleccion == 2:
        iva = precio_sin_iva * 10/100
        print("El precio total es: " + str(importe_final3(precio_sin_iva,iva)))
    
    elif seleccion == 3:
        iva = precio_sin_iva * 4/100
        print("El precio total es: " + str(importe_final3(precio_sin_iva,iva)))



