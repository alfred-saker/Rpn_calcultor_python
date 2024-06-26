import pytest
from main import rpn_calculate

def test_rpn_single_number():
    assert rpn_calculate("42") == 42

def test_rpn_basic_operations():
    assert rpn_calculate("3 4 +") == 7
    assert rpn_calculate("10 5 -") == 5
    assert rpn_calculate("2 3 *") == 6

def test_rpn_complex_expression():
    assert rpn_calculate("5 1 2 + 4 * + 3 -") == 14

