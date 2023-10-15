from src.ejercicio8 import nivel

def test_nivel():
    assert nivel(0.3) == "Su nivel es inaceptable, su dinero es 2400"
    assert nivel(0.5) == "Su nivel es aceptable, su dinero es 3360"
    assert nivel(0.8) == "Su nivel es meritorio, su dinero es 3840"
    
