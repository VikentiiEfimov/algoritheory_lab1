_lod = None
_violator_songs = None
_target_songs = []

def inp_lod():
    global _lod, _violator_songs
    print("1. Список\n2. Словарь")
    tp = int(input("Введите тип данных: "))
    _lod = True if tp == 1 else False
    _violator_songs = [] if _lod else {}
    print(f"Тип установлен") 

def inp_violator():
    global _violator_songs, _lod
    song = input("Введите название песни: ")
    time = float(input("Введите время её звучания: "))
    if _lod: _violator_songs.append([song, time])
    else: _violator_songs.update({song : time})
    print(f"Песня довавлена")

def inp_target():
    global _target_songs
    print("Введённые песни")
    enumeration = _violator_songs if _lod else _violator_songs.items()
    fin = []
    for index, (n, _) in enumerate(enumeration):
        fin.append([index,n])
        print(f'{index+1}. {n}')   
    ind = (input("Введите номера выбранных песен: "))
    for nd in ind.split(", "):
        _target_songs.append(next(n for (i,n) in fin if int(nd)-1 == i))
    #_target_songs.append(_violator_songs[int(nd) - 1][0]if _lod else _violator_songs[fin[]] (name for name,_ in _violator_songs[] if nd in target_songs))
    print(f"Выбраны песни: {', '.join(_target_songs)}")

def nwch():
    global _target_songs
    _target_songs.clear()
    print("Выбор стёрт")

def nwps():
    global _violator_songs
    _violator_songs.clear()
    nwch()
    print("Данные почищены")

def reset():
    global _lod
    _lod = None
    nwps()
    print("Тип сброшен")

def compute(violator_songs, target_songs):
    tm = sum([time for song, time in violator_songs if song in target_songs])
    return f"Песни звучат {round(tm, 3)} минут"

def otp_totime():
    print(compute(_violator_songs if _lod 
                  else _violator_songs.items(), 
                  _target_songs))


def get_menu():
    current_menu = {}
    if _lod is None: 
        current_menu['1'] = ('Ввести тип данных', inp_lod)
    elif len(_violator_songs) == 0:
        current_menu['2'] = ('Ввести песню', inp_violator)
    elif len(_target_songs) == 0:
        current_menu['3'] = ('Следующая песня', inp_violator)
        current_menu['4'] = ('Выбрать песню', inp_target)
    else:
        current_menu['4'] = ('Выбрать след.песню', inp_target)
        current_menu['5'] = ('Вывести общее время звучания вырбанных песен', otp_totime)
        current_menu['7'] = ('Сбросить всё', reset)     
    current_menu['0'] = ('Выход', None)
    return current_menu

mock_data = iter(['1', '1', 
                  '2','World in My Eyes','4.86',
                  '3','Sweetest Perfection','4.43',
                  '3','Personal Jesus','4.56',
                  '3','Halo','4.9',
                  '3','Waiting for the Night','6.07',
                  '3','Enjoy the Silence','4.20',
                  '3','Policy of Truth','4.76',
                  '3','Blue Dress','4.29',
                  '3','Clean','5.83',
                  '4','4, 6, 9',
                  '5',
                  '7',
                  '1','2',
                  '2','World in My Eyes','4.86',
                  '3','Sweetest Perfection','4.43',
                  '3','Personal Jesus','4.56',
                  '3','Halo','4.9',
                  '3','Waiting for the Night','6.07',
                  '3','Enjoy the Silence','4.20',
                  '3','Policy of Truth','4.76',
                  '3','Blue Dress','4.29',
                  '3','Clean','5.83',
                  '4','2, 7, 8',
                  '5',
                  '7'])