def pan_fresco(cantidad,descuento_pan):
    return(cantidad * descuento_pan)


if __name__ == "__main__":
    
 PAN = 3.49

 cantidad = int(input("Introduce la cantidad de barras no frescas vendidad: "))

 descuento_pan = 3.49-(3.49*0.60)

 print("El coste final de barras no frescas es: " + str(round(pan_fresco(cantidad,descuento_pan),2)) + " Euros")