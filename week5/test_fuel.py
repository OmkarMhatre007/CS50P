import pytest
from fuel import convert, gauge

def test_str():
    with pytest.raises(ValueError):
        convert("lion")

def test_denzero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_negative():
    with pytest.raises(ValueError):
        convert("-2/-4")
    with pytest.raises(ValueError):
        convert("3/-6")
    with pytest.raises(ValueError):
        convert("-4/8")

def test_num_greater():
    with pytest.raises(ValueError):
        convert("9/3")

def test_percentage():
    assert convert("1/2") == 50
    assert convert("4/4") == 100

def test_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_fuel_percentage():
    assert gauge(50) == "50%"
    assert gauge(34) == "34%"
