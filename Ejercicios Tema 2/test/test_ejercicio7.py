from src.ejercicio7 import renta

def test_renta():
    assert renta(23) == "Impositivo del 5%"
    assert renta(10000) == "Impositivo del 15%"
    assert renta(20000) == "Impositivo del 20%"
    assert renta(35000) == "Impositivo del 30%"
    assert renta(60000) == "Impositivo del 45%"