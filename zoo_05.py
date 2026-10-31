def run():
    # Есть список животных в зоопарке
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

    # Посадите медведя (bear) между львом и кенгуру
    apply_action(zoo, 'insert', 1, 'bear')
    # и выведите список на консоль
    print(zoo)

    # Добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark']
    apply_action(zoo, 'extend', birds)
    # и выведите список на консоль
    print(zoo)

    # Уберите слона (elephant) из зоопарка
    apply_action(zoo, 'remove', 'elephant')
    # и выведите список на консоль
    print(zoo)

    #добавить кролика в центр и посадить в клетку
    apply_action(zoo, 'insert', len(zoo) // 2, 'rabbit')  
    print(zoo)
    print(f"Кролик сидит в клетке №{cage_number(zoo, 'rabbit')}")

    # Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    print(f"Лев сидит в клетке №{cage_number(zoo, 'lion')}")
    print(f"Жаворонок сидит в клетке №{cage_number(zoo, 'lark')}")

def apply_action(zoo, action: str, *args):
    getattr(zoo, action)(*args)

def cage_number(zoo: list[str], animal: str) -> int:
    # Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
    return zoo.index(animal) + 1

if __name__ == "__main__":
    run()