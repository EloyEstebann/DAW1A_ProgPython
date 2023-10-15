from src.ejercicio9 import entrada

def test_entrada():
    assert entrada(2) == "Entrada gratis!!"
    assert entrada(23) == "Entrada 10 euros!!"
    assert entrada(12) == "Entrada 5 euros!!"