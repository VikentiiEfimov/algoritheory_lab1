opera = {
    1 : ["плюс", '+'],
    2 : ["минус", '-'], 
    3 : ["умножение", '*'],
    4 : ["скобка_on", '('],
    5 : ["скобка_off", ')'],
    6 : ["пусто", ' ']
}

_numbers = []
_opeations = []
_position = 0

def inp_number():
    global _numbers, _opeations, _position
    inp = input("Есть числа: ")
    for nb in inp.split(", "):
        _numbers.append(nb)
    _opeations = [''] * (len(_numbers)+1)  #только для закрывающей скобки
    #_position = 0
    print(f"Числа обозначены. Всего чисел: {len(_numbers)}")
    
def reset():
    global _position, _numbers, _opeations
    _position = 0
    _numbers = []
    _opeations = []
    print("Данные пусты")


def add_sinn():
    global _position, _opeations
    print("Оперы")
    for index in opera.keys():
        print(f'{index}. {opera[index][0]}')
    ind = int(input(f"Введите знак перед <{_position + 1}-ым> числом: "))
    oper = opera[ind][1]
    _opeations[_position] += f' {oper}'
    print(f"Добавлен знак <{oper}>")


def est_nxt():
    global _position
    _position += 1
    print(f"Переход на <{_position + 1}-ое> число")

def compute(numbers, placement):
    expression = []
    for (numb, signs) in zip(numbers, placement):
        expression.append(f'{signs} {numb} ')
    e = ''.join(expression)
    return f"{e} = {eval(e)}"

def otp_xprs():
    print(compute(_numbers, _opeations))


def get_menu():
    current_menu = {}
    #if len(_numbers)==0: 
    current_menu['1'] = ('Ввести числа', inp_number)
    current_menu['2'] = ('Добавить знак перед числом', add_sinn)
    current_menu['3'] = ('Перейти к следующему числу', est_nxt)
    current_menu['4'] = ('Сосчитать выражение', otp_xprs)

    current_menu['7'] = ('Сброс', reset)     
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','1, 2, 3',
                  '2','4',
                  '3', '2','1',
                  '3', '2','5', '2','3',
                  '4',
                  '7',
                  '1','1, 2, 3, 4, 5',
                  '2','4', '2','4',
                  '3', '2','3',
                  '3', '2','1',
                  '3', '2','5', '2','3',
                  '3', '2','5', '2','1',
                  '4'])