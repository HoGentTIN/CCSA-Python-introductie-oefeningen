import pytest
from reeks_4b_recursieve_functies.fibonacci import fib

@pytest.mark.timeout(1)
def test_fib_0():
    assert fib(0) == 0

@pytest.mark.timeout(1)
def test_fib_1():
    assert fib(1) == 1

@pytest.mark.timeout(1)
def test_fib_2():
    assert fib(2) == 1

@pytest.mark.timeout(1)
def test_fib_3():
    assert fib(3) == 2

@pytest.mark.timeout(1)
def test_fib_11():
    assert fib(11) == 89

@pytest.mark.timeout(1)
def test_fib_30():
    assert fib(30) == 832040