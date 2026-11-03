def run():
    cross = {
        #   первое слово - 4-я буква
        0 : [3, 4, 1],
        #   второе слово - буквы с 10 по 13, включительно
        1 : [9, 13, 1],
        #   третье слово - буквы с 6 по 15, включительно, через одну
        2 : [5, 14, 2],
        #   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
        3 : [12, 6, -1],
        #   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
        4 : [20, 15, -1]
    }

    for stroka, position in cross.items():
        print(next(compute(stroka, position[0], position[1], position[2])), end=" ")
    print()

def compute(po, bg, nd, st):
    # Есть зашифрованное сообщение
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    yield secret_message[po][bg:nd:st]





_NOISE = "abcdefghijklmnopqrstuvwxyz0123456789"
_WORD_LEN = 32

_phrase = None
_words = []
_encoded = []
_cross = {}
_pos = 0
_rule = None
_step = None
_p1 = None
_p2 = None


def _noise(n):
    # детерминированный "дым": одинаковый для mock и для ручного ввода
    return ''.join(_NOISE[i % len(_NOISE)] for i in range(n))


def _build(word, rule, step, p1, p2):
    # p1, p2 — 1-based номера "первой" и "последней" букв блока в строке из 32
    # возвращает (encoded, bg, nd, st) или (None, ошибка)
    L = len(word)
    pos_start = p1 - 1
    if rule == 'normal':
        if p2 - p1 + 1 != L:
            return None, "длина слова не совпадает с (последняя - первая + 1)"
        slice_bg, slice_nd, st = pos_start, p2, 1
        placed = word
        positions = list(range(pos_start, pos_start + L))
    elif rule == 'step':
        if step is None or step < 1:
            return None, "шаг должен быть >= 1"
        if p2 - p1 + 1 != (L - 1) * step + 1:
            return None, "шаг не совпадает с (последняя - первая)"
        slice_bg, slice_nd, st = pos_start, p2, step
        placed = word
        positions = [pos_start + i * step for i in range(L)]
    elif rule == 'reverse':
        if p2 - p1 + 1 != L:
            return None, "длина слова не совпадает с (последняя - первая + 1)"
        slice_bg, slice_nd, st = p2 - 1, p1 - 2, -1
        placed = word[::-1]
        positions = list(range(pos_start, pos_start + L))
    else:
        return None, "правило не выбрано"
    if positions[0] < 0 or positions[-1] >= _WORD_LEN:
        return None, f"слово не влезает в {_WORD_LEN} символов"
    chars = list(_noise(_WORD_LEN))
    for pos, ch in zip(positions, placed):
        chars[pos] = ch
    return (''.join(chars), slice_bg, slice_nd, st), "ok"


def inp_phrase():
    global _phrase, _words, _encoded, _cross, _pos
    _phrase = input("Введите фразу: ")
    _words = _phrase.split()
    _encoded = []
    _cross = {}
    _pos = 0
    print(f"Фраза обозначена. Слов: {len(_words)}")
    for i, w in enumerate(_words):
        print(f"  {i+1}. <{w}> ({len(w)} букв)")


def inp_rule():
    global _rule, _step
    print("Правила порядка:")
    print("  1. обычный")
    print("  2. с шагом")
    print("  3. в обратном")
    choice = input("Выбор: ").strip()
    if choice == '1':
        _rule, _step = 'normal', 1
    elif choice == '2':
        _rule = 'step'
        _step = int(input("Введите шаг: "))
    elif choice == '3':
        _rule, _step = 'reverse', -1
    else:
        print("Нет такого правила")
        return
    print(f"Правило установлено: {_rule}")


def inp_first():
    global _p1
    _p1 = int(input(f"Введите номер первой буквы слова <{_words[_pos]}>: "))
    print(f"Первая: {_p1}")


def inp_last():
    global _p2, _rule, _step, _p1, _encoded, _cross, _pos
    _p2 = int(input(f"Введите номер последней буквы слова <{_words[_pos]}>: "))
    print(f"Последняя: {_p2}")
    res, msg = _build(_words[_pos], _rule, _step, _p1, _p2)
    if res is None:
        print(f"Ошибка: {msg}. Попробуйте снова.")
        _p2 = None
        return
    encoded, bg, nd, st = res
    _encoded.append(encoded)
    _cross[_pos] = [bg, nd, st]
    print(f"Слово <{_words[_pos]}> зашифровано: {encoded}")
    print(f"  cross[{_pos}] = [{bg}, {nd}, {st}]")
    _pos += 1
    _rule = None
    _step = None
    _p1 = None
    _p2 = None


def compute(idx):
    bg, nd, st = _cross[idx]
    return _encoded[idx][bg:nd:st]


def otp_encoded():
    print("Зашифрованные строки:")
    for i, s in enumerate(_encoded):
        print(f"  {i+1}. {s}")


def otp_decoded():
    parts = [compute(i) for i in range(len(_words))]
    print(f"Расшифровано: {' '.join(parts)}")


def reset():
    global _phrase, _words, _encoded, _cross, _pos, _rule, _step, _p1, _p2
    _phrase = None
    _words = []
    _encoded = []
    _cross = {}
    _pos = 0
    _rule = None
    _step = None
    _p1 = None
    _p2 = None
    print("Данные пусты")


def get_menu():
    current_menu = {}
    if _phrase is None:
        current_menu['1'] = ('Ввести фразу', inp_phrase)
    elif _pos >= len(_words):
        current_menu['5'] = ('Вывести зашифрованное', otp_encoded)
        current_menu['6'] = ('Вывести расшифрованное', otp_decoded)
        current_menu['7'] = ('Сброс', reset)
    else:
        if _rule is None:
            current_menu['2'] = ('Выбрать правило', inp_rule)
        elif _p1 is None:
            current_menu['3'] = ('Ввести первую букву', inp_first)
        else:
            current_menu['4'] = ('Ввести последнюю букву', inp_last)
        current_menu['7'] = ('Сброс', reset)
    current_menu['0'] = ('Выход', None)
    return current_menu


mock_data = iter([
    '1', 'мама мыла раму',
    '2', '1', '3', '3', '4', '6',            # мама: normal, 3..6
    '2', '2', '2', '3', '3', '4', '9',        # мыла: step=2, 3..9
    '2', '3', '3', '3', '4', '6',             # раму: reverse, 3..6
    '5', '6', '7', '0',
])