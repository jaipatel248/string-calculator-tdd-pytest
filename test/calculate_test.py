import pytest
import sys
from src.calculate import calculateString

def test_empty_string():
    assert calculateString("") == 0

def test_single_number():
    assert calculateString("1") == 1
    assert calculateString("12") == 12