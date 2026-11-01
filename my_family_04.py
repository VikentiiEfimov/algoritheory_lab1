_role = None
_height = None
_my_family_height = []
_target = None

def inp_role():
    global _role, _height
    _role = input("Введите члена семьи: ")
    _height = None
    print(f"Роль <{_role}> обозачена")

def inp_height():
    global _height, _role, _my_family_height
    _height = float(input("Введите его рост: "))
    _my_family_height.append([_role, _height])
    print(f"Рост установлен: {_height}")

def establish():
    global _role
    _role = None
    
def reset():
    global _my_family_height
    _my_family_height.clear()
    establish()
    print("Список пуст")

def otp_list():
    global _target
    print("Моя семья")
    for index, (n, _) in enumerate(_my_family_height):
        print(f'{index+1}. {n}')
    ind = int(input("Введите номер выбранного члена семьи: "))
    _target = _my_family_height[ind - 1][0]
    print(f"Выбрана цель: {_target}")

def compute(title, aggregate):
    return f'{title} - {aggregate(_my_family_height)} см'

def otp_target_mfh():
    otp_list()
    print(compute('Её рост', lambda h: next(v for n, v in h if n == _target)))

def otp_all_mfh():
    print(compute('Общий рост моей семьи', lambda h: sum(v for _, v in h)))


def get_menu():
    current_menu = {}
    if _role is None: current_menu['1'] = ('Ввести роль', inp_role)
    elif _height is None:
        current_menu['2'] = ('Ввести X', inp_height)
    else:
        current_menu['3'] = ('Следующий член семьи', establish)
        current_menu['4'] = ('Вывести рост выбранного члена моей семьи', otp_target_mfh)
        current_menu['5'] = ('Вывести общий рост моей семьи', otp_all_mfh)
        current_menu['6'] = ('Сбросить список', reset)     
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','папа', 
                    '2','189', 
                '3', 
                '1','мама', 
                    '2','170', 
                '3', 
                '1','я', 
                    '2','187',
                '3', 
                '1','бабушка', 
                    '2','160',
                '3', 
                '1','дедушка', 
                    '2','172',
                '3', 
                '1','сестра', 
                    '2','165',
                '4', '1',
                '5'
                ])