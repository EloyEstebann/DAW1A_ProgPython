def precioproducto(precio):
    euro , centimo = precio.split(".")
    return "El precio del producto es " + euro + " euros y " + centimo + " centimos."

if __name__ == "__main__":
    precio = input("Introduce el precio en este formato rr.xx: ")
    print(precioproducto(precio))