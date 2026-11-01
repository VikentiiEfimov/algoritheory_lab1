_my_favorite_movies = None
_movies = []

def inp_flm():
    global _my_favorite_movies, _movies
    _my_favorite_movies = input("Есть перечисление фильмов: ")
    _movies = [movie for movie in _my_favorite_movies.split(", ")]
    print(f"Фильмы обозначены")

def get_bounds(movie_index):
    global _movies
    start = sum(len(_movies[i]) + 2 for i in range(movie_index))
    end = start + len(_movies[movie_index])
    return (start, end)

def compute(index):
    global _my_favorite_movies
    bg, nd = get_bounds(index)
    return _my_favorite_movies[bg:nd]

def reset():
    global _my_favorite_movies, _movies
    _my_favorite_movies = None
    _movies = []
    print("Данные пусты")

def otp_per():
    print(f"Первый - {compute(0)}") #0,10

def otp_pos():
    print(f"Последний - {compute(len(_movies)-1)}") #42,57

def otp_vtr():
    print(f"Второй - {compute(1)}") #12,25

def otp_prd():
    print(f"Предпоследний - {compute(len(_movies)-2)}") #35,40


def get_menu():
    current_menu = {}
    if _my_favorite_movies is None: 
        current_menu['1'] = ('Ввести фильмы', inp_flm)
    else:
        current_menu['2'] = ('Вывести первый фильм', otp_per)
        current_menu['3'] = ('Вывести последний фильм', otp_pos)
        if len(_movies) >=2:
            current_menu['4'] = ('Вывести второй фильм', otp_vtr)
            current_menu['5'] = ('Вывести предпоследний фильм', otp_prd)
        current_menu['6'] = ('Сбросить перечень', reset)     
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее',
                  '2', '3', '4', '5'])