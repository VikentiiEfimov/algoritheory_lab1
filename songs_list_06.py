def run():
    # Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]

    # Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
    #   Три песни звучат ХХХ минут
    # Обратите внимание, что суммирование чисел с плавающей точкой может давать погрешность,
    # округлите результат до 3 знаков после запятой
    target_songs = ['Halo', 'Enjoy the Silence', 'Clean']
    list_time = sum([song[1] for song in violator_songs_list if song[0] in target_songs])
    print(f"Три песни звучат {round(list_time, 3)} минут")


    # Есть словарь песен группы Depeche Mode
    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }

    # Распечатайте общее время звучания трех других песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
    # в формате
    #   А другие три песни звучат ХХХ минут
    # Обратите внимание на округление
    other_songs = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    dict_time = sum([time for song, time in violator_songs_dict.items() if song in other_songs])
    print(f'А другие три песни звучат {round(dict_time, 3)} минут')
    
if __name__ == "__main__":
    run()