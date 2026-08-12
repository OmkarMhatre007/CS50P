from numb3rs import validate

def test_dot():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3") == False
    assert validate("123.213.1.5.6") == False

def test_limit():
    assert validate("255.255.255.255") == True
    assert validate("512.512.1.34") == False
    assert validate("1.2.3.1000") == False

def test_extra_zeros():
    assert validate("192.168.002.1") == False
    assert validate("1.2.3.40") == True
    assert validate("01.02.03.04") == False

def test_words():
    assert validate("cat") == False
    assert validate("127.cat.8.bat") == False
    assert validate("one.eight.7.98") == False
