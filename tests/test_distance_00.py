from distance_00 import compute


def test_two_cities():
    result = compute({'A': (0, 0), 'B': (3, 4)})
    assert result['A']['B'] == 5.0
    assert result['B']['A'] == 5.0


def test_symmetric_and_no_self():
    sites = {'Moscow': (550, 370), 'London': (510, 510), 'Paris': (480, 480)}
    result = compute(sites)
    assert result['Moscow']['London'] == result['London']['Moscow']
    assert result['Moscow']['London'] == 145.6
    for city, neighbors in result.items():
        assert city not in neighbors  # нет расстояния до самого себя


def test_single_city():
    assert compute({'Solo': (1, 1)}) == {'Solo': {}}