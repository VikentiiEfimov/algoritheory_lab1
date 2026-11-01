from my_family_04 import compute


def test_father_height():
    result = compute('Рост отца', lambda h: next(v for n, v in h if n == 'папа'))
    assert result == 'Рост отца - 189 см'


def test_total_height():
    result = compute('Общий рост', lambda h: sum(v for _, v in h))
    assert result == 'Общий рост - 1043 см'


def test_custom_aggregate():
    # проверяем, что агрегат действительно применяется
    result = compute('Кол-во', lambda h: len(h))
    assert result == 'Кол-во - 6 см'