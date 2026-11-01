from shopping_09 import compute


def test_single_item():
    sweets = {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
    }
    result = list(compute(sweets))
    assert len(result) == 1
    assert 'печенье' in result[0]
    assert 'пятерочка' in result[0]
    assert '9.99' in result[0]
    assert 'ашан' in result[0]
    assert '10.99' in result[0]


def test_multiple_items():
    sweets = {
        'a': [{'shop': 'A', 'price': 1.0}, {'shop': 'B', 'price': 2.0}],
        'b': [{'shop': 'C', 'price': 3.0}, {'shop': 'D', 'price': 4.0}],
    }
    result = list(compute(sweets))
    assert len(result) == 2
    assert 'a' in result[0] and 'b' in result[1]


def test_two_shops_per_item():
    sweets = {
        'a': [{'shop': 'A', 'price': 1.0}, {'shop': 'B', 'price': 2.0}],
    }
    result = list(compute(sweets))
    # в каждом блоке ровно 2 магазина
    assert result[0].count('стоит') == 2