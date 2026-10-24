def run():
    # Есть список животных в зоопарке
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

    # Посадите медведя (bear) между львом и кенгуру
    # и выведите список на консоль
    zoo.insert(1, 'bear')
    print(zoo)

    # Добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark']
    # и выведите список на консоль
    zoo.extend(birds)
    print(zoo)

    # Уберите слона (elephant) из зоопарка
    # и выведите список на консоль
    zoo.remove('elephant')
    print(zoo)

    # Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
    lion_index = zoo.index('lion') + 1
    lark_index = zoo.index('lark') + 1

    #добавить кролика в центр и посадить в клетку
    zoo.insert(3, 'rabbit')
    rabbit_index = zoo.index('rabbit') + 1
    print(zoo)
    print(f'Кролик сидит в клетке №{rabbit_index}')

    print(f'Лев сидит в клетке №{lion_index}')
    print(f'Жаворонок сидит в клетке №{lark_index}')

if __name__ == "__main__":
    run()