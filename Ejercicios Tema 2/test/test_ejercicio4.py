from src.ejercicio4 import par_impar

def test_par_impar():
    assert par_impar(20) == "El número es par"
    assert par_impar(19) == "El número es impar"