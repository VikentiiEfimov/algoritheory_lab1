_city = None
_x = None
_y = None
_sites = {}

def inp_city():
    global _city, _x, _y
    _city = input("Введите название города: ")
    _x = None
    _y = None
    print(f"Город {_city} обозачен")

def inp_iks():
    global _x
    _x = float(input("Введите координату X для города: "))
    print(f"X установлен: {_x}")

def inp_igr():
    global _y, _x, _sites, _city
    _y = float(input("Введите координату Y для города: "))
    _sites[_city] = (_x, _y)
    print(f"Y установлен: {_y}")

def establish():
    global _city
    _city = None
    
def reset():
    global _sites, _city,  _x, _y
    _sites.clear()
    _city = None
    _x = None
    _y = None
    print("Словарь пуст")

def distances(sites):
    distances = {}
    for city1, coord1 in sites.items():
            distances[city1] = {}
            x1, y1 = coord1   
            for city2, coord2 in sites.items():
                if city1 == city2: continue
                x2, y2 = coord2
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = round(distance, 2)
    return distances

def otp_dist():
    print(f"Словарь расстояний между городами:\n{distances(_sites)}")


def get_menu():
    current_menu = {}
    if _city is None: current_menu['1'] = ('Ввести город', inp_city)
    if _city is not None:
        if _x is not None and _y is not None:
            current_menu['4'] = ('Следующий город', establish)
            if len(_sites.keys())>=2:
                current_menu['5'] = ('Вывести словарь', otp_dist)
            current_menu['6'] = ('Сбросить словарь', reset)
        else:
            if _x is None:
                current_menu['2'] = ('Ввести X', inp_iks)
            else:
                current_menu['3'] = ('Ввести Y', inp_igr)
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','Moscow', 
                    '2','550', '3','370', 
                    '4', 
                '1','London', 
                    '2','510', '3','510', 
                    '4',
                '1','Paris', 
                    '2','480', '3','480', 
                    '5'])