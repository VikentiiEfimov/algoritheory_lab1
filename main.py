from distance_00 import run as run_00
from circle_01 import run as run_01
from operations_02 import run as run_02 
from favorite_movies_03 import run as run_03
from my_family_04 import run as run_04
from zoo_05 import run as run_05
from songs_list_06 import run as run_06
from secret_07 import run as run_07
from garden_08 import run as run_08
from shopping_09 import run as run_09
from store_10 import run as run_10


TASKS = {
    "00": ("Расстояние", run_00),
    "01": ("Окружность", run_01),
    "02": ("Операции", run_02),
    "03": ("Любимые фильмы", run_03),
    "04": ("Моя семья", run_04),
    "05": ("Зоопарк", run_05),
    "06": ("Список песен", run_06),
    "07": ("Секрет", run_07),
    "08": ("Сад", run_08),
    "09": ("Покупки", run_09),
    "10": ("Склад", run_10),
}

def run_task(key):
    title, func = TASKS[key]
    print(f"\n=== {key}: {title} ===")
    func()

def main():
    for key in TASKS:
        run_task(key)

if __name__ == "__main__":
    print(f"{'='*22}\nВерхнеуровневый модуль\n{'='*22}")
    main()