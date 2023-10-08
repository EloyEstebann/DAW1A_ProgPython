
def correccion(email):
    usuario,domino = email.split("@")
    return usuario


if __name__ == "__main__":
    email = input("Introduce tu email: ")
    print(correccion(email) + "@ceu.es")