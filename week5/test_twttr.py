from twttr import shorten

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_lowercase():
    assert shorten("google") == "ggl" 

def test_spaces():
    assert shorten("Hello World") == "Hll Wrld"

def test_punctuation():
    assert shorten("hi!") == "h!"

def test_numbers():
    assert shorten("12345") == "12345"
