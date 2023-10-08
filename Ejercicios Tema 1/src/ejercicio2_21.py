def lecturainversa(frase):
    palabras = frase.split()
    palabras_inversas = reversed(palabras)
    frase_inversa = " ".join(palabras_inversas)
    return frase_inversa

if __name__ == "__main__":
    frase = input("Introduce una frase: ")
    print(lecturainversa(frase)) 
