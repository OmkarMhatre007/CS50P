import pytest
from working import convert

def test_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:26 AM to 2:43 PM") == "09:26 to 14:43"

def test_hours():
    with pytest.raises(ValueError):
        convert("13:20 AM to 8 PM")
    with pytest.raises(ValueError):
        convert("8 AM to 14:40 PM")
    assert convert("8 AM to 3 PM") == "08:00 to 15:00"
    assert convert("6 PM to 1 AM") == "18:00 to 01:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"

def test_zeros():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 6 AM") == "00:00 to 06:00"
    assert convert("11 PM to 12:15 AM") == "23:00 to 00:15"
