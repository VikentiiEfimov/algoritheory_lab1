_radius = None
_x = None
_y = None

def inp_rad():
    global _radius, _x, _y
    _radius = float(input("Введите радиус круга: "))
    _x = None
    _y = None
    print(f"Радиус установлен: {_radius}")

def inp_iks():
    global _x
    _x = float(input("Введите координату X для точки: "))
    print(f"X установлен: {_x}")

def inp_igr():
    global _y
    _y = float(input("Введите координату Y для точки: "))
    print(f"Y установлен: {_y}")
    
def area(r):
    pi = 3.1415926
    area = pi * (r ** 2)
    return round(area, 4)

def otp_area():
    print(f"Площадь круга: {area(_radius)}")

def point(r, x, y):
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance <= r

def otp_pnt():
    print(f"Точка внутри круга?: {point(_radius, _x, _y)}")

def reset_point():
    global _x, _y
    _x = None
    _y = None
    print("Координаты точки сброшены. Введите X и Y заново.")


def get_menu():
    current_menu = {}
    current_menu['1'] = ('Ввести радиус', inp_rad)
    if _radius is not None:
        current_menu['2'] = ('Вывести площадь', otp_area)
        if _x is not None and _y is not None:
            current_menu['5'] = ('Проверить точку', otp_pnt)
            current_menu['6'] = ('Сбросить точку', reset_point)
        else:
            if _x is None:
                current_menu['3'] = ('Ввести X', inp_iks)
            else:
                current_menu['4'] = ('Ввести Y', inp_igr)
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','42', 
                '2', 
                    '3','23', 
                    '4','34', 
                '5', 
                '6', 
                    '3','30',
                    '4','30', 
                '5'])