def run():
    print(compute('Рост отца',
                  lambda h: next(v for n, v in h if n == 'папа')))
    print(compute('Общий рост моей семьи',
                  lambda h: sum(v for _, v in h)))
    
def compute(title, aggregate):
    # Создайте списки:
    # моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
    #my_family = ['папа', 'мама', 'я', 'бабушка', 'дедушка', 'сестра']

    # список списков приблизительного роста членов вашей семьи
    my_family_height = [
        ['папа', 189],
        ['мама', 170],
        ['я', 187],
        ['бабушка', 160],
        ['дедушка', 172],
        ['сестра', 165]
    ]
    return f'{title} - {aggregate(my_family_height)} см'

if __name__ == "__main__":
    run()