def run():
    # В саду сорвали цветы
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

    # На лугу сорвали цветы
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

    # Создайте множество цветов, произрастающих в саду и на лугу
    # garden_set =
    # meadow_set =
    garden_set = set(garden)
    meadow_set = set(meadow)

    # Выведите на консоль все виды цветов
    all_flowers = garden_set | meadow_set
    print('Все виды цветов:', ', '.join(sorted(all_flowers)))

    # Выведите на консоль те, которые растут и там и там
    common_flowers = garden_set & meadow_set
    print('Растут и в саду, и на лугу:', ', '.join(sorted(common_flowers)))

    # Выведите на консоль те, которые растут в саду, но не растут на лугу
    only_garden = garden_set - meadow_set
    print('Только в саду:', ', '.join(sorted(only_garden)))

    # Выведите на консоль те, которые растут на лугу, но не растут в саду
    only_meadow = meadow_set - garden_set
    print('Только на лугу:', ', '.join(sorted(only_meadow)))

if __name__ == "__main__":
    run()