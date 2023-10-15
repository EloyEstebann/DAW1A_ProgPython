

def elegir_ingrediente(lista_ingredientes):
    print("Ingredientes disponibles: ", ", ".join(lista_ingredientes))
    return input("Elija un ingrediente: ")

        
if __name__ == "__main__":
    print("¡Bienvenido a la pizzería Bella Napoli!")
    tipo_pizza = input("¿Desea una pizza vegetariana (V) o no vegetariana (NV)? ").upper()

    
    ingredientes_base = ["Mozzarella", "Tomate"]
    ingredientes_vegetarianos = ["pimiento", "tofu"]
    ingredientes_no_vegetarianos = ["peperoni", "jamón", "salmón"]
    
    # Elegir el tipo pizza
    
    if tipo_pizza == "V":
        ingrediente_elegido = elegir_ingrediente(ingredientes_vegetarianos)
        if ingrediente_elegido in ingredientes_vegetarianos:
            ingredientes_base.append(ingrediente_elegido)
            print("\nHas elegido una pizza vegetariana con los siguientes ingredientes: ", ", ".join(ingredientes_base))
        else:
            print("El ingrediente elegido no es válido.")
            
    elif tipo_pizza == "NV":
        ingrediente_elegido = elegir_ingrediente(ingredientes_no_vegetarianos)
        if ingrediente_elegido in ingredientes_no_vegetarianos:
            ingredientes_base.append(ingrediente_elegido)
            print("\nHas elegido una pizza no vegetariana con los siguientes ingredientes: ", ", ".join(ingredientes_base))
        else:
            print("El ingrediente elegido no es válido.")
            
    else:
        print("Opción no válida.")
