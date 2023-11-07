import math


def raiz(n):
    return math.sqrt(n)


def test_raiz():
    assert raiz(9) == 3
    assert raiz(81) == 9
    assert raiz(144) == 12
    assert raiz(400) == 20
    assert raiz(196) == 14


class Poesia:
    def __init__(self, titulo, autor, versos):
        self.titulo = titulo
        self.autor = autor
        self.versos = versos

    def num_versos(self):
        return len(self.versos)

    def recitar(self, verso_num):
        try:
            return self.versos[verso_num]
        except IndexError:
            return "Verso não encontrado"


def test_recitar():
    poema = Poesia("Soneto de Separação", "Vinícius de Moraes", [
        "De repente do riso fez-se o pranto",
        "Silencioso e branco como a bruma",
        "E das bocas unidas fez-se a espuma",
        "E das mãos espalmadas fez-se o espanto."
    ])

    assert poema.recitar(0) == "De repente do riso fez-se o pranto"
    assert poema.recitar(1) == "Silencioso e branco como a bruma"
    assert poema.recitar(4) == "Verso não encontrado"


def greet(name):
    return f"Hello: {name}"


def test_greet():
    assert greet("World") == "Hello: World"
    assert greet("1") == "Hello: 1"


class Calculator:
    def add(self, x, y):
        return x + y


def test_calculator():

    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-4, 7) == 3
