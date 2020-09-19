import pytest

from src.model.mock_ops import add, multiply, subtract


def test_multiply():
    result = multiply(2, 3)
    assert result == 6


def test_add():
    result = add(2, 4)
    assert result == 6


def test_subtract():
    result = subtract(3, 3)
    assert result == 0
