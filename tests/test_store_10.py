from store_10 import compute


def test_single_batch():
    goods = {'Лампа': '111'}
    store = {'111': [{'quantity': 27, 'price': 42}]}
    assert list(compute(goods, store)) == ['Лампа - 27 шт, стоимость 1134 руб']


def test_multiple_batches():
    goods = {'Стол': '222'}
    store = {'222': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ]}
    # 22*510 + 32*520 = 27860
    assert list(compute(goods, store)) == ['Стол - 54 шт, стоимость 27860 руб']


def test_multiple_goods():
    goods = {'A': '1', 'B': '2'}
    store = {
        '1': [{'quantity': 5, 'price': 10}],
        '2': [{'quantity': 2, 'price': 100}, {'quantity': 3, 'price': 50}],
    }
    assert list(compute(goods, store)) == [
        'A - 5 шт, стоимость 50 руб',
        'B - 5 шт, стоимость 350 руб',
    ]


def test_empty_store():
    assert list(compute({}, {})) == []