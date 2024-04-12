def suma(a: int, b: int) -> int:
    return a + b

def resta(a: int, b: int) -> int:
    return a - b

def test_suma():
    respuesta = suma(3, 4)
    assert respuesta == 7

def test_resta():
    respuesta = resta(10, 5)
    assert respuesta == 5