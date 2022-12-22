from lib import calc
import pytest


@pytest.fixture()
def plus():
    return 5, '+', 5


@pytest.fixture()
def minus():
    return 10, '-', 10
# задаем числа и знак действия



@pytest.fixture()
def umnozh():
    return 4, '*', 5

@pytest.fixture()
def delen():
    return 10, '/', 10

@pytest.fixture()
def error():
    return '+', '-', '+'

# тест плюса
def testplus(plus):
    assert calc(*plus) == 10

# тест минуса
def testminus(minus):
    assert calc(*minus) == 0

# тест умножения
def testumnozhenine(umnozh):
    assert calc(*umnozh) == 20

# тест деления
def testdelenie(delen):
    assert calc(*delen) == 1

def testerror(error):
    with pytest.raises(TypeError):
        calc(error)