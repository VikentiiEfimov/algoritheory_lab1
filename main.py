from favorite_movies_03 import get_menu as menu_03, mock_data as mock_03


TASKS = {
    "03": ("Любимые фильмы", menu_03, mock_03),
}

_wring = True
def wring(menu):
    print()
    for k, (t, _) in menu.items(): print(f"{k}. {t}")
# для отладки:__builtins__.input  __builtins__["input"]

def run_task(key):
    global _wring
    title, menu_getter, mock = TASKS[key]
    print(f"\n=== {key}: {title} ===")
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
    for key in TASKS:
        run_task(key)

if __name__ == "__main__":
    print("=" * 22)
    print("Верхнеуровневый модуль")
    print("=" * 22)
    main()