from src.ejercicio2 import comprobacion

def test_comprobacion():
  assert comprobacion("contraseña","contraseña") == "La contraseña es correcta"
  assert comprobacion("contraseña","123") == "La contraseña no es correcta"