import operator

from garden_08 import flowers


def test_all_flowers():
    remark, result = flowers('Все виды цветов:', operator.or_)
    assert remark == 'Все виды цветов:'
    assert result == 'гладиолус, клевер, мак, одуванчик, подсолнух, роза, ромашка'


def test_common_flowers():
    _, result = flowers('', operator.and_)
    assert result == 'одуванчик, ромашка'


def test_only_garden():
    _, result = flowers('', operator.sub)
    assert result == 'гладиолус, подсолнух, роза'


def test_only_meadow():
    _, result = flowers('', operator.sub, reverse=True)
    assert result == 'клевер, мак'


def test_sorted_output():
    # результат всегда отсортирован
    _, result = flowers('', operator.or_)
    assert result == ', '.join(sorted(result.split(', ')))