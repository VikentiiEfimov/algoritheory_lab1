from favorite_movies_03 import compute


def test_first_movie():
    assert compute(0, 10) == 'Терминатор'


def test_last_movie():
    assert compute(42, 57) == 'Назад в будущее'


def test_second_movie():
    assert compute(12, 25) == 'Пятый элемент'


def test_second_from_end():
    assert compute(35, 40) == 'Чужие'


def test_no_comma_in_output():
    for bounds in [(0, 10), (12, 25), (35, 40), (42, 57)]:
        assert ',' not in compute(*bounds)