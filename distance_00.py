def run():
    # Есть словарь координат городов
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    print(compute(sites))

def compute(sites):
    # Составим словарь словарей расстояний между ними
    distances = {}
    for city1, coord1 in sites.items():
            distances[city1] = {}
            x1, y1 = coord1   
            for city2, coord2 in sites.items():
                if city1 == city2: continue
                x2, y2 = coord2
                # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = round(distance, 2)
    return distances

if __name__ == "__main__":
    run()