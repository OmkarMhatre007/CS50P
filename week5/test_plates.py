from plates import is_valid

def test_alnum():
    assert is_valid("CS50") == True
    assert is_valid("Rob2.0") == False
    assert is_valid("KA-30") == False

def test_len():
    assert is_valid("MH10") == True
    assert is_valid("GJAM102") == False
    assert is_valid("C") == False

def test_twoalpha():
    assert is_valid("CS50") == True
    assert is_valid("SSD10") == True
    assert is_valid("A7") == False
    assert is_valid("1A") == False
    assert is_valid("11ABC") == False
    assert is_valid("8DA40") == False

def test_1stzero():
    assert is_valid("CS50") == True
    assert is_valid("MH01") == False

def test_endnum():
    assert is_valid("CS50") == True
    assert is_valid("CS100") == True
    assert is_valid("CS50P") == False
