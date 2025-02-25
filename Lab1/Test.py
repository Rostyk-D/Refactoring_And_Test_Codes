import pytest
import pylint
import flake8

from main import (
    NOT, AND, OR, IMP, EQU,
    complex_statement, build_truth_table
)
# Тестування функцій логічних операцій
def test_not():
    assert NOT(0) == 1
    assert NOT(1) == 0

def test_and():
    assert AND(0, 0) == 0
    assert AND(1, 0) == 0
    assert AND(1, 1) == 1

def test_or():
    assert OR(0, 0) == 0
    assert OR(1, 0) == 1
    assert OR(1, 1) == 1

def test_imp():
    assert IMP(0, 0) == 1
    assert IMP(0, 1) == 1
    assert IMP(1, 0) == 0
    assert IMP(1, 1) == 1

def test_equ():
    assert EQU(0, 0) == 1
    assert EQU(1, 1) == 1
    assert EQU(0, 1) == 0
    assert EQU(1, 0) == 0

# Тестування складного виразу
def test_complex_statement():
    assert complex_statement(1, 0, 1) == 1

def test_complex_statement1():
    assert complex_statement(0, 1, 0) == 0

def test_complex_statement2():
    assert complex_statement(1, 1, 0) == 0

def test_complex_statement3():
    assert complex_statement(0, 0, 0) == 0

# Тестування таблиці істинності
def test_truth_table():
    table = build_truth_table()
    assert len(table) == 10
    for row in table:
        A, B, C, result = row
        assert result in [0, 1]
