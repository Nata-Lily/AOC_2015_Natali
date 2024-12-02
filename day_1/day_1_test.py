import pytest

from day_1 import find_floor, first_down_basement


def test_find_floor1():
    assert 0 == find_floor("(())")


def test_find_floor2():
    assert 0 == find_floor("()()")


def test_find_floor3():
    assert 3 == find_floor("(((")


def test_find_floor4():
    assert 3 == find_floor("(()(()(")


def test_find_floor5():
    assert 3 == find_floor("))(((((")


def test_find_floor6():
    assert -1 == find_floor("())")


def test_find_floor7():
    assert -1 == find_floor("))(")


def test_find_floor8():
    assert -3 == find_floor(")))")


def test_find_floor9():
    assert -3 == find_floor(")())())")


def test_find_floor10():
    assert 1000 == find_floor('('*1000)


def test_first_down_basement1():
    assert 5 == first_down_basement("(()))")


def test_first_down_basement2():
    assert 1 == first_down_basement(")")


def test_first_down_basement3():
    assert None is first_down_basement("(((")


def test_first_down_basement4():
    assert 11 == first_down_basement("(()(()())))")
