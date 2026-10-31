def run():
    # Выведите на консоль с помощью индексации строки, последовательно:
    # Запятая не должна выводиться. Переопределять my_favorite_movies нельзя.

    #   первый фильм
    print(compute(0,10))
    #   последний
    print(compute(42,57))
    #   второй
    print(compute(12,25))
    #   второй с конца
    print(compute(35,40))
    
def compute(bg, nd):
    # Есть строка с перечислением фильмов
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    return my_favorite_movies[bg:nd]

if __name__ == "__main__":
    run()