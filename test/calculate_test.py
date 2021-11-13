import pytest
import sys
from src.calculate import calculateString

def test_empty_string():
    assert calculateString("") == 0