# -*- coding: utf-8 -*-

import pytest
from calculator.calculator import count, Operation

op1 = Operation(1, 2, '+')
op2 = Operation(4, 3, '-')
op3 = Operation(5, 4, '*')
op4 = Operation(9, 3, '/')
op5 = Operation(9, 3, '&')

def test_count():
    assert count(1, 2, '+') == 3.0
    assert count(4, 3, '-') == 1.0
    assert count(5, 4, '*') == 20.0
    assert count(9, 3, '/') == 3.0
    with pytest.raises(SystemExit):
        count(9, 3, '&')

def test_get_result():
    assert op1.get_result() == 3.0
    assert op2.get_result() == 1.0
    assert op3.get_result() == 20.0
    assert op4.get_result() == 3.0
    with pytest.raises(SystemExit):
        op5.get_result()