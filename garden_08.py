import operator
def run():
    # Выведите на консоль все виды цветов
    print(*flowers('Все виды цветов:', operator.or_))

    # Выведите на консоль те, которые растут и там и там
    print(*flowers('Растут и в саду, и на лугу:', operator.and_))

    # Выведите на консоль те, которые растут в саду, но не растут на лугу
    print(*flowers('Только в саду:', operator.sub))

    # Выведите на консоль те, которые растут на лугу, но не растут в саду
    print(*flowers('Только на лугу:', operator.sub, reverse=True))

def flowers(remark, op, reverse=False):
    # В саду сорвали цветы
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

    # На лугу сорвали цветы
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

    # Создайте множество цветов, произрастающих в саду и на лугу
    # garden_set =
    # meadow_set =
    garden_set = set(garden)
    meadow_set = set(meadow)

    a, b = (meadow_set, garden_set) if reverse else (garden_set, meadow_set)
    return remark, ', '.join(sorted(op(a, b)))

if __name__ == "__main__":
    run()