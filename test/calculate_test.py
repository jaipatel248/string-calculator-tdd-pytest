import pytest
import sys
from src.calculate import calculateString

def test_empty_string():
    assert calculateString("") == 0

def test_single_number():
    assert calculateString("1") == 1
    assert calculateString("12") == 12

def test_two_numbers():
    assert calculateString("1,2") == 3
    assert calculateString("12,34") == 46

def test_multiple_numbers():
    assert calculateString("1,2,3") == 6
    assert calculateString("5,6,7,8,9") == 35

def test_new_line():
    assert calculateString("1\n2\n3") == 6
    assert calculateString("1\n2\n3\n4") == 10

def test_new_line_and_comma():
    assert calculateString("1\n2,3") == 6
    assert calculateString("1\n2,3\n4") == 10

def test_delimiter():
    assert calculateString("//;\n1;2") == 3
    assert calculateString("//:\n1:5") == 6
    assert calculateString("///\n2/5") == 7
    assert calculateString("//abc\n2abc5") == 7

def test_negative_number():
	with pytest.raises(Exception, match = r'negatives not allowed -1,-2'):
		calculateString("1,2,3,-1,-2")
