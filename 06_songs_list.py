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
for song in violator_songs_list:
    if song[0] == 'Halo':
        halo_time = song[1]
    elif song[0] == 'Enjoy the Silence':
        enjoy_time = song[1]
    elif song[0] == 'Clean':
        clean_time = song[1]

total_time_list = halo_time + enjoy_time + clean_time
print(f'Три песни звучат {round(total_time_list, 3)} минут')


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
sweet_time = violator_songs_dict['Sweetest Perfection']
policy_time = violator_songs_dict['Policy of Truth']
blue_time = violator_songs_dict['Blue Dress']

total_time_dict = sweet_time + policy_time + blue_time
print(f'А другие три песни звучат {round(total_time_dict, 3)} минут')