import pytest

#Ejercicio 1
from src.ejercicio2_1 import saludo

def test_saludo():
    assert saludo("Paco") == "Bienvenido Paco" 

#Ejercicio 2
from src.ejercicio2_2 import importe_total

def test_importe_total():
    assert importe_total(2,1) == 2

#Ejercicio 3
from src.ejercicio2_3 import operacionuno,operaciondos,operaciontres
def test_operacionuno():
    assert operacionuno(2) == 1

def test_operaciondos():
    assert operaciondos(2) == 1

def test_operaciontres():
    assert operaciontres(9) == 3

#Ejercicio 4
from src.ejercicio2_4 import calculo

def test_calculo():
    assert calculo(25) == 77

#Ejercicio 5
from src.ejercicio2_5 import importe_final1,importe_final2,importe_final3



def test_importe_final1():
    assert importe_final1(121,0) == 121

def test_importe_final2():
    assert importe_final2(110,0) == 110

def test_importe_final3():
    assert importe_final3(104,0) == 104


#Ejercicio 6
from src.ejercicio2_6 import iva_pagado,importe_siniva


def test_iva_pagado():
    assert iva_pagado(100) == 10

def test_importe_siniva():
    assert importe_siniva(100,10) == 90


#Ejercicio 7
from src.ejercicio2_7 import suma

@pytest.mark.parametrize(
    "input_x, input_y, input_z, expected",
    [
        (1,1,1,3),
        (0,0,0,0),
        (200,-100,50,150),
        (-10,20,-9,1),
        (2*4,2,5,15),
    ]
)

def test_suma_params(input_x, input_y, input_z, expected):
    assert suma(input_x, input_y, input_z) == expected


#Ejercicio 8
from src.ejercicio2_8 import suma2

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (1,1,5),
        (0,0,3),
        (200,-100,103),
        (-10,20,13),
        (2*4,2,13),
    ]
)

def test_suma2_params(input_x, input_y, expected):
    assert suma2(input_x, input_y) == expected


#Ejercicio 9
from src.ejercicio2_9 import suma3

def test_suma3():
    assert suma3() == 10


#Ejercicio 10
from src.ejercicio2_10 import operacion_aritmetica

def test_operacionaritmetica():
    assert operacion_aritmetica() == 0.25


#Ejercicio 11
"""from ejercicio2_11 import suma_entero

def test_suma_entero():
    assert suma_entero(1) == 1"""

#Ejercicio 12

from src.ejercicio2_12 import indicecorporal

@pytest.mark.parametrize(
    "input_peso, input_estatura, expected",
    [
        (4,2,1.00),
        (48,1.67,17.21108680841909),
        (55,1.69,19.257028815517668),
        (45.2342,23,0.08550888468809074),
        (23,2.234,4.608520232205301),
    ]
)

def test_indicecorporal(input_peso, input_estatura, expected):
    assert indicecorporal(input_peso, input_estatura) == expected


#Ejercicio2_13
from src.ejercicio2_13 import cociente,resto

def test_cociente():
    assert cociente(4,2) == 2

def test_resto():
    assert resto(9,2) == 1


#Ejercicio 2_14
from src.ejercicio2_14 import peso_total

@pytest.mark.parametrize(
    "input_payaso, input_muñeca, expected",
    [
        (1,1,187),
        (2,4,524),
        (5,33,3035),
        (24,547,43713),
        (3242,345,388979),
    ]
)

def test_peso_total(input_payaso, input_muñeca, expected):
    assert peso_total(input_payaso, input_muñeca) == expected


#Ejercicio 2_15
from src.ejercicio2_15 import cantidad_final

def test_cantidad_final():
    assert cantidad_final(100) == 274.4


#Ejercicio 2_16
from src.ejercicio2_16 import pan_fresco

def test_pan_fresco():
    assert pan_fresco(4,1.396) == 5.584


#Ejercicio 2_17
from src.ejercicio2_17 import bucle

def test_bucle():
    assert bucle("Eloy",2) == "Eloy\nEloy\n"

#Ejercicio 2_18
from src.ejercicio2_18 import resultado_nombre

def test_resultado_nombre():
    nombrecompleto = "manuel ruiz"
    nombre_minusculas, nombre_mayusculas, nombre_final = resultado_nombre(nombrecompleto)
    assert nombre_minusculas  == "manuel ruiz"
    assert nombre_mayusculas  == "MANUEL RUIZ"
    assert nombre_final  == "ManuelRuiz"
    
    
#Ejercicio 2_19
from src.ejercicio2_19 import resultado_nombre_final

def test_resultado_nombre_final():
    assert resultado_nombre_final("Paco") == "Tu nombre es: PACO y tiene 4 letras"

#Ejercicio 2_20
from src.ejercicio2_20 import numerotelefono

def test_numerotelefono():
    assert numerotelefono("34-676834551") == "676834551"

#Ejercicio 2_21
from src.ejercicio2_21 import lecturainversa

def test_lecturainversa():
    assert lecturainversa("Hola me llamo Pepe") == "Pepe llamo me Hola"

#Ejercicio 2_22
from src.ejercicio2_22 import transformacion

def test_transformacion():
    assert transformacion("hola me llamo pepe", "a") == "holA me llAmo pepe"


#Ejercicio 2_23
from src.ejercicio2_23 import correccion

def test_correccion():
    assert correccion("micorreo@xxxxx.com") == "micorreo"


#Ejercicio 2_24
from src.ejercicio2_24 import precioproducto

def test_precioproducto():
    precioproducto("22.33") == "El precio del producto es 22 euros y 23 centimos."

"""#Ejercicio 2_25
from src.ejercicio2_25 import fecha"""

#Ejercicio 2_26
from src.ejercicio2_26 import lista_de_compra

def test_lista_de_compra():
    assert lista_de_compra("filetes,cereza,patata") == "filetes\ncereza\npatata\n"

