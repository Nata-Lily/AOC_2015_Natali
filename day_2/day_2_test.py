import pytest

from day_2 import find_square_wrapping_paper


def test_find_square_wrapping_paper1():
    assert 58 == find_square_wrapping_paper("2x3x4")


def test_find_square_wrapping_paper2():
    assert 43 == find_square_wrapping_paper("1x1x10")


def test_find_square_wrapping_paper3():
    assert 7 == find_square_wrapping_paper("1x1x1")
