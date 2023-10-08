def lista_de_compra(lista):
    productos = lista.split(",")
    resultado = ""
    for producto in productos:
        resultado += producto.strip() + "\n"
    return resultado

if __name__ =="__main__":
    lista = input("Introduce la lista de la compra separada por comas: ")

    print(lista_de_compra(lista))
  