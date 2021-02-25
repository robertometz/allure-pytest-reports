import pytest


def func(x):
    return x + 1


def test_func():
    assert func(1) == 2


def test_func_error():
    assert func(1) == 3


def test_func_ignored():
    pytest.skip('Ignored!')
