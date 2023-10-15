from src.ejercicio1 import funcionedad

def test_funcionedad():
    assert funcionedad(23) == "Soy mayor de edad!!"
    assert funcionedad(12) == "Soy menor de edad!!"
