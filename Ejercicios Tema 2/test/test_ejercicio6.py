from src.ejercicio6  import determinar_grupo

def test_determinar_grupo():
    assert determinar_grupo("Paco","H") == "Tu grupo es el A"
    assert determinar_grupo("Eloy","H") == "Tu grupo es el B"
    assert determinar_grupo("Laura","H") == "Tu grupo es el B"
    assert determinar_grupo("Sofia","H") == "Tu grupo es el A"