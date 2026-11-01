from operations_02 import compute


def test_example_123_9():
    result = list(compute([1, 2, 3], ['(', '+', ') *']))
    assert len(result) == 1
    assert result[0].endswith('= 9')


def test_main_12345_25():
    result = list(compute([1, 2, 3, 4, 5], ['( (', '*', '+', ') *', ') +']))
    assert result[0].endswith('= 25')


def test_expression_is_valid():
    # проверяем, что eval-часть действительно даёт число
    out = next(compute([1, 2, 3], ['(', '+', ') *']))
    left, right = out.rsplit('=', 1)
    assert int(right.strip()) == 9