import pytest

from zoo_05 import apply_action, cage_number


def test_insert_bear():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    apply_action(zoo, 'insert', 1, 'bear')
    assert zoo == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']


def test_extend_birds():
    zoo = ['lion', 'kangaroo']
    apply_action(zoo, 'extend', ['rooster', 'ostrich', 'lark'])
    assert zoo == ['lion', 'kangaroo', 'rooster', 'ostrich', 'lark']


def test_remove():
    zoo = ['lion', 'elephant', 'monkey']
    apply_action(zoo, 'remove', 'elephant')
    assert zoo == ['lion', 'monkey']


def test_cage_number_one_indexed():
    zoo = ['lion', 'bear', 'kangaroo']
    assert cage_number(zoo, 'lion') == 1
    assert cage_number(zoo, 'kangaroo') == 3


def test_cage_number_missing():
    with pytest.raises(ValueError):
        cage_number(['lion'], 'tiger')  