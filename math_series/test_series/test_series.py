import pytest
from series.series import fibonnaci
from series.series import lucas
from series.series import sum_series

def test_one():
    actual = fibonnaci(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = fibonnaci(0)
    expected = 0
    assert actual == expected

def test_three():
    actual = fibonnaci(2)
    expected = 1
    assert actual == expected

def test_four():
    actual = fibonnaci(6)
    expected = 8
    assert actual == expected

def test_five():
    actual = fibonnaci(-6)
    expected = -6
    assert actual == expected

def test_six():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_seven():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_eight():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_nine():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_nine():
    actual = lucas(-8)
    expected = -8
    assert actual == expected

def test_ten():
    actual = sum_series(4, first =3 , second =2)
    expected = 12
    assert actual == expected

def test_eleven():
    actual = lucas(-9)
    expected = -9
    assert actual == expected

def test_twelve():
    actual = sum_series(6)
    expected = 8
    assert actual == expected