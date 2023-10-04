import pytest

#Ejercicio 1
from ejercicio2_1 import saludo

def test_saludo():
    assert saludo("Paco") == "Bienvenido Paco" 

#Ejercicio 2
from ejercicio2_2 import importe_total

def test_importe_total():
    assert importe_total(2,1) == 2

#Ejercicio 3
from ejercicio2_3 import operacionuno

def test_operacionuno():
    assert operacionuno(2) == 1

