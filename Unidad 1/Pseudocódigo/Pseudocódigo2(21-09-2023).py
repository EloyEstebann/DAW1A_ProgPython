# Lee el primer número
numero1 = int(input("Introduce el primer número: "))

# Lee el segundo número
numero2 = int(input("Introduce el segundo número: "))

# Genera y muestra la serie
if numero1 <= numero2:
    serie = list(range(numero1, numero2 + 1))
else:
    serie = list(range(numero2, numero1 + 1))

print("La serie entre los números es:", serie)
