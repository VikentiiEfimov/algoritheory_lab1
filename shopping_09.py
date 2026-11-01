_name = None
_shop = None
_price = None
_sweets = {}

def inp_sweet():
    global _name, _shop, _price, _sweets
    _name = input("Введите сладость: ")
    _shop = None
    _price = None
    _sweets[_name] = []
    print(f"Сладость обозначена: {_name}")

def inp_shop():
    global _shop
    _shop = input("Введите магазин: ")
    print(f"Магазин обозначен: {_shop}")

def inp_price():
    global _name, _shop, _price, _sweets
    _price = float(input("Введите цену: ")) 
    _sweets[_name].append({'shop': _shop, 'price': _price})
    print(f"Цена установлена: {_price}")

def establish_g():
    global _shop, _price; _shop = _price = None

def establish_v():
    global _name; _name = None
    establish_g()

def reset():
    global _sweets
    _sweets.clear()
    establish_v()
    print("Список пуст")

def compute(sweets):
    print("Сладости в 2 магазинах с минимальными ценами")
    for name, shoprice in sweets.items():
        comm = f'{name}\n'
        for sp in shoprice:
            comm += f' - в "{sp["shop"]}" стоит {sp["price"]} руб.'
        yield comm

def otp_cmm():
    for comm in compute(_sweets): 
        print(comm)


def get_menu():
    current_menu = {}
    if _name is None:
        current_menu['1'] = ('Ввести сладость', inp_sweet)
    elif _shop is None:
        current_menu['2'] = ('Ввести магазин', inp_shop)
    elif _price is None:
        current_menu['3'] = ('Ввести цену', inp_price)
    else:
        current_menu['4'] = ('Следующие магазин/цена', establish_g)
        current_menu['5'] = ('Следующая сладость', establish_v)
        current_menu['6'] = ('Вывести распродажу', otp_cmm)
        current_menu['7'] = ('Сбросить список', reset)  
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter([  '1','печенье', 
                '2','пятерочка',
                '3','9.99', 
                    '4',
                '2','ашан',
                '3','10.99', 
                    '5',
                    '1','конфеты', 
                '2','магнит',
                '3','30.99', 
                    '4',
                '2','пятерочка',
                '3','32.99', 
                    '5',
                    '1','карамель', 
                '2','магнит',
                '3','41.99', 
                    '4',
                '2','ашан',
                '3','45.99', 
                    '5',
                    '1','пирожное', 
                '2','пятерочка',
                '3','59.99', 
                    '4',
                '2','магнит',
                '3','62.99', 
                    '6'])