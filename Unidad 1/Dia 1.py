#Variable y tipo (Integer, Float, String, Boleanos, Listas, Tuplas, Diccionarios,...)
#Literal por ejemplo--> numeroUno = 1
#Operadores = + - *
#Funcion: print(argumentos de la función), str(...), ...


numeroUno = 1
numeroDos = 3
numeroTres = "4" #Cadena por estar en comillas
mensaje = "El resultado de la suma es "

def suma(numeroUno:int, numeroDos:int) -> int:
    return numeroUno + numeroDos

resultadoSuma = suma(numeroUno, numeroDos)
print(mensaje + str(resultadoSuma))

