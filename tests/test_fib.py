# Тест чисел Фибоначчи
import pytest
from src.lib import Fibonacci
class test_fib:
    #тест с n = 10
    def testOne(self):
        assert Fibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # тест c n = 0, вызывает исключение IndexError.
    def testTwo(self):
        with pytest.raises(IndexError):
            Fibonacci(0)
