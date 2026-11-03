from distance_00 import get_menu as menu_00, mock_data as mock_00
from circle_01 import get_menu as menu_01, mock_data as mock_01
from operations_02 import get_menu as menu_02, mock_data as mock_02
from favorite_movies_03 import get_menu as menu_03, mock_data as mock_03
from my_family_04 import get_menu as menu_04, mock_data as mock_04
from zoo_05 import get_menu as menu_05, mock_data as mock_05
from songs_list_06 import get_menu as menu_06, mock_data as mock_06
#from secret_07 import get_menu as menu_07, mock_data as mock_07
from garden_08 import get_menu as menu_08, mock_data as mock_08
from shopping_09 import get_menu as menu_09, mock_data as mock_09
from store_10 import get_menu as menu_10, mock_data as mock_10


TASKS = {
    "00": ("Расстояние", menu_00, mock_00),
    "01": ("Окружность", menu_01, mock_01),
    "02": ("Операции", menu_02, mock_02),
    "03": ("Любимые фильмы", menu_03, mock_03),
    "04": ("Моя семья", menu_04, mock_04),
    "05": ("Зоопарк", menu_05, mock_05),
    "06": ("Список песен", menu_06, mock_06),
    #"07": ("Секрет", menu_07, mock_07),
    "08": ("Сад", menu_08, mock_08),
    "09": ("Покупки", menu_09, mock_09),
    "10": ("Склад", menu_10, mock_10),
}

_wring = True
def wring(menu):
    print()
    for k, (t, _) in menu.items(): print(f"{k}. {t}")
# для отладки:__builtins__.input  __builtins__["input"]

def run_task(key):
    global _wring
    title, menu_getter, mock = TASKS[key]
    print(f"\n\n=== {key}: {title} ===")
    original_input = __builtins__.input
    while True:
        menu = menu_getter()
        if _wring: wring(menu)
        choice = input("Выбор: ").strip() 
        if choice == '-1':
            print("\nВЫВОД ЗАГЛУШКИ")
            _wring = False
            def mock_input(prompt=""):
                global _wring
                try:
                    return next(mock)
                except StopIteration:
                    _wring = True; wring(menu)
                    __builtins__.input = original_input
                    return original_input(prompt)
            __builtins__.input = mock_input
            continue
        else:
            entry = menu.get(choice)
            if entry is None:
                print("Нет такого пункта")
                continue
            if entry[1] is None:
                break
            entry[1]()

def main():
    while True:
        print("\nДоступные задачи:")
        for key, entry in TASKS.items():
            print(f"  {key}. {entry[0]}")
        print("  all — запустить все, q — выход")

        choice = input("Выбор: ").strip().lower()

        if choice in ("q", "quit", "exit", ""):
            break
        if choice == "all":
            for key in TASKS:
                run_task(key)
            continue
        if choice in TASKS:
            run_task(choice)
        else:
            print("Нет такой задачи")

if __name__ == "__main__":
    print("=" * 22)
    print("Верхнеуровневый модуль")
    print("=" * 22)
    main()