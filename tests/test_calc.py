import pytest
from calc_for_tests_2 import calc

def test_plus():
    assert calc('2 + 3') == 5

def test_minus():
    assert calc('4 - 5') == -1

def test_mult():
    assert calc('6 * 5') == 30

def test_div():
    assert calc('15 / 3') == 5

def test_nosigns():
    with pytest.raises(ValueError) as error:
        calc('aaa')
    assert 'Вираз повинен містити хоча б один знак (+-/*)' == error.value.args[0]

def test_twosigns():
    with pytest.raises(ValueError) as error:
        calc('1+1+')
    assert 'Вираз повинен містити два цілих числа і тільки один знак' == error.value.args[0]

if __name__ == '__main__':
    pytest.main()
