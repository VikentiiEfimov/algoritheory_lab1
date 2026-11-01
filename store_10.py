_name = None
_quantity = None
_price = None
_store = {}

def inp_goods():
    global _name, _quantity, _price, _store
    _name = input("Введите товар: ")
    _quantity = None
    _price = None
    _store[_name] = []
    print(f"Товар обозначен: {_name}")

def inp_quant():
    global _quantity
    _quantity = int(input("Введите количество: "))
    print(f"Количество установлено: {_quantity}")

def inp_price():
    global _name, _quantity, _price, _store
    _price = int(input("Введите цену: ")) 
    _store[_name].append({'quantity': _quantity, 'price': _price})
    print(f"Цена установлена: {_price}")

def establish_g():
    global _quantity, _price; _quantity = _price = None

def establish_v():
    global _name; _name = None
    establish_g()

def reset():
    global _store
    _store.clear()
    establish_v()
    print("Список пуст")

def compute(store):
    for name, batches in store.items():
        total_quantity = 0
        total_cost = 0
        for batch in batches:
            total_quantity += batch['quantity']
            total_cost += batch['quantity'] * batch['price']
        yield f'{name} - {total_quantity} шт, стоимость {total_cost} руб'

def otp_itm():
    for item in compute(_store):
        print(item)

def get_menu():
    current_menu = {}
    if _name is None:
        current_menu['1'] = ('Ввести товар', inp_goods)
    elif _quantity is None:
        current_menu['2'] = ('Ввести количество', inp_quant)
    elif _price is None:
        current_menu['3'] = ('Ввести цену', inp_price)
    else:
        current_menu['4'] = ('Следующие количество/цена', establish_g)
        current_menu['5'] = ('Следующий товар', establish_v)
        current_menu['6'] = ('Вывести склад', otp_itm)
        current_menu['7'] = ('Сбросить список', reset)  
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter([  '1','Лампа', 
                '2','27',
                '3','42',  
                    '5',
                    '1','Стол', 
                '2','22',
                '3','510', 
                    '4',
                '2','32',
                '3','520', 
                    '5',
                    '1','Диван', 
                '2','2',
                '3','1200', 
                    '4',
                '2','1',
                '3','1150', 
                    '5',
                    '1','Стул', 
                '2','50',
                '3','100', 
                    '4',
                '2','12',
                '3','95', 
                    '4',
                '2','43',
                '3','97',
                    '6'])
