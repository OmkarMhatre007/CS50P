import pytest
from jar import Jar


def test_init():
    jar1 = Jar()
    jar2 = Jar(3)
    assert jar1.capacity == 12
    assert jar2.capacity == 3
    with pytest.raises(ValueError):
        Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    jar.deposit(2)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)
        jar.deposit(-3)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    jar.withdraw(3)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(4)
        jar.withdraw(-3)
