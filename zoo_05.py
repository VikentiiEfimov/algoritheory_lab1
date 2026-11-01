_position = None
_beast = None
_zoo = []
_birds = []

def inp_zoo():
    global _zoo
    inp = input("Есть животные в зоопарке: ")
    for zo in inp.split(", "):
        _zoo.append(zo)
    print(f"Животные обозначены")
    
def reset():
    global _position, _beast, _zoo, _birds
    _position = _beast = None
    _zoo = _birds = []
    print("Данные пусты")

def est_posad():
    global _beast, _position
    _beast = input("Введите нового зверя: ")
    _position = int(input("Введите его позицию"))
    apply_action('insert',_position, _beast)

def est_last():
    global _birds
    _birds.clear()
    birds = input("Введите птиц в последние клекти: ")
    for br in birds.split(", "):
        _birds.append(br)
    apply_action('extend', _birds)

def est_uber():
    global _beast
    _beast = input("Введите зверя для удаления: ")
    apply_action('remove', _beast)

def apply_action(action: str, *args):
    getattr(_zoo, action)(*args)

def cage_number(animal):
    return _zoo.index(animal) + 1

def otp_ndx():
    bist = input("Введите зверя корректно: ")
    print(f"Тот некий зверь сидит в клетке №{cage_number(bist)}")

def otp_zoo():
    print(_zoo)


def get_menu():
    current_menu = {}
    if len(_zoo)==0: 
        current_menu['1'] = ('Ввести животных', inp_zoo)
    else:
        current_menu['2'] = ('Вывести зоопарк', otp_zoo)
        current_menu['3'] = ('Посадить зверя', est_posad)
        current_menu['4'] = ('Добавить птиц', est_last)
        current_menu['5'] = ('Убрать зверя', est_uber)
        current_menu['6'] = ('Вывести номер', otp_ndx)
        current_menu['7'] = ('Перебить зоопарк', reset)     
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','lion, kangaroo, elephant, monkey', '2',
                  '3','bear','1', '2',
                  '4','rooster, ostrich, lark', '2',
                  '5','elephant', '2',
                  '3','rabbit', '3', '2',
                  '6','rabbit', '6','lion', '6','lark'])