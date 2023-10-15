from src.ejercicio5 import tributar

def test_tributar():
    assert tributar(1600,16) == "Puede tributar"
    assert tributar(1600,15) == "No puede tributar"
    assert tributar(213,16) == "No puede tributar"
    assert tributar(123,11) == "No puede tributar"
    assert tributar(2435,35) == "Puede tributar"
    