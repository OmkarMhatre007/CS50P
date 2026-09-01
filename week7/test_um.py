import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("..um") == 1
    assert count("um...") == 1

def test_um_sentence():
    assert count("um, thanks for the album.") == 1
    assert count("What was the number, um...") == 1
    assert count("Hello everyone") == 0
    assert count("um, Food is yummy") == 1

def test_multiple_um():
    assert count("um, Hello, um, World") == 2
    assert count("Um, thanks, um...") == 2

def test_ignore_case():
    assert count("Um, thank you") == 1
    assert count("UM, I was going to go to the grocery store, but, um, I completely forgot my wallet at home.") == 2
