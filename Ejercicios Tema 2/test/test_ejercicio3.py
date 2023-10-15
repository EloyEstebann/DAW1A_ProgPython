from src.ejercicio3 import calculadora

def test_calculadora():
    assert calculadora(20,0) == "Error!!"
    assert calculadora(20,2) == 10.00