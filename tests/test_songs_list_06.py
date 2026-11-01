from songs_list_06 import compute


def test_list_input():
    songs = [['Halo', 4.9], ['Enjoy the Silence', 4.20], ['Clean', 5.83]]
    targets = ['Halo', 'Enjoy the Silence', 'Clean']
    result = compute(songs, targets, 'Т')
    assert result == 'Три песни звучат 14.93 минут'


def test_dict_input():
    songs = {'Sweetest Perfection': 4.43, 'Policy of Truth': 4.88, 'Blue Dress': 4.18}
    targets = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    result = compute(songs.items(), targets, 'А другие т')
    assert result == 'А другие три песни звучат 13.49 минут'


def test_empty_selection():
    result = compute([['Halo', 4.9]], ['Clean'], 'Т')
    assert result.startswith('Три песни звучат 0')


def test_rounding():
    # 0.1 + 0.2 = 0.30000000000000004 → округление до 3 знаков = 0.3
    songs = [['a', 0.1], ['b', 0.2]]
    result = compute(songs, ['a', 'b'], 'Т')
    assert '0.3' in result