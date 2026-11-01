import operator
_garden_set = None
_meadow_set = None

def inp_garden():
    global _garden_set
    gar = []
    den = input("В саду сорвали цветы: ")
    for flow in den.split(", "):
        gar.append(flow)
    _garden_set = set(gar)
    print(f"Сад обозачен")

def inp_meadow():
    global _meadow_set
    mea = []
    dow = input("На лугу сорвали цветы: ")
    for flow in dow.split(", "):
        mea.append(flow)
    _meadow_set = set(mea)
    print(f"Луг обозачен")
    
def reset():
    global _garden_set, _meadow_set
    _garden_set = None
    _meadow_set = None
    print("Множества пусты")

def flowers(remark, op, reverse=False):
    a, b = (_meadow_set, _garden_set) if reverse else (_garden_set, _meadow_set)
    return remark, ', '.join(sorted(op(a, b)))

def otp_or():
    print(*flowers('Все виды цветов:', operator.or_))

def otp_and():
    print(*flowers('Растут и в саду, и на лугу:', operator.and_))

def otp_sub():
    print(*flowers('Только в саду:', operator.sub))

def otp_reversub():
    print(*flowers('Только на лугу:', operator.sub, reverse=True))


def get_menu():
    current_menu = {}
    if _garden_set is None: 
        current_menu['1'] = ('Ввести сад', inp_garden)
    elif _meadow_set is None:
        current_menu['2'] = ('Ввести луг', inp_meadow)
    else:
        current_menu['3'] = ('Вывести на консоль все виды цветов', otp_or)
        current_menu['4'] = ('Вывести на консоль те, которые растут и там и там', otp_and)
        current_menu['5'] = ('Вывести на консоль те, которые растут в саду, но не растут на лугу', otp_sub)
        current_menu['6'] = ('Вывести на консоль те, которые растут на лугу, но не растут в саду', otp_reversub)
        current_menu['7'] = ('Сбросить множества', reset)     
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1','ромашка, роза, одуванчик, ромашка, гладиолус, подсолнух, роза', 
                  '2','клевер, одуванчик, ромашка, клевер, мак, одуванчик, ромашка', 
                '3','4','5','6'])