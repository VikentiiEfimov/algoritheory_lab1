# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

cities = list(sites.keys())

for i in range(len(cities)):
    city1 = cities[i]
    x1, y1 = sites[city1]
    
    if city1 not in distances:
        distances[city1] = {}
    
    for j in range(i + 1, len(cities)):
        city2 = cities[j]
        x2, y2 = sites[city2]
        
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        
        distances[city1][city2] = distance
        if city2 not in distances:
            distances[city2] = {}
        distances[city2][city1] = distance

print(distances)
