import pytest
from seasons import check_birthday_date

def test_valid_date_format():
    assert check_birthday_date("2011-06-30") == ("2011", "06", "30")
    assert check_birthday_date("1999-02-20") == ("1999", "02", "20")
    with pytest.raises(ValueError):
        check_birthday_date("20001-24-09")
    with pytest.raises(ValueError):
        check_birthday_date("2002-123-30")
    with pytest.raises(ValueError):
        check_birthday_date("May 10 2014")

