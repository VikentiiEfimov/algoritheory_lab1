from secret_07 import compute


def test_word_1():
    assert list(compute(0, 3, 4, 1)) == ['в']


def test_word_2():
    assert list(compute(1, 9, 13, 1)) == ['бане']


def test_word_3():
    assert list(compute(2, 5, 14, 2)) == ['веник']


def test_word_4():
    assert list(compute(3, 12, 6, -1)) == ['дороже']


def test_word_5():
    assert list(compute(4, 20, 15, -1)) == ['денег']


def test_full_phrase():
    cross = {0: [3, 4, 1], 1: [9, 13, 1], 2: [5, 14, 2], 3: [12, 6, -1], 4: [20, 15, -1]}
    phrase = [next(compute(po, *args)) for po, args in cross.items()]
    assert phrase == ['в', 'бане', 'веник', 'дороже', 'денег']