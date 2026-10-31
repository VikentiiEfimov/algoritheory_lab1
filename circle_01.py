def run():
    # Выведите на консоль значение площади этого круга с точностью до 4-х знаков после запятой
    print(compute(area, None))

    # Далее, пусть есть координаты точки
    point_1 = (23, 34)
    # где 23 - координата х, 34 - координата у
    print(compute(point, point_1))

    # Аналогично для другой точки
    point_2 = (30, 30)
    print(compute(point, point_2))


def compute(obj, p):
    # Есть значение радиуса круга
    radius = 42
    return obj(radius,p)


def area(r, p=None):
    pi = 3.1415926
    area = pi * (r ** 2)
    return round(area, 4)


def point(r, p):
    x = p[0]; y = p[1]
    distance = (x ** 2 + y ** 2) ** 0.5
     # Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
    is_inside = distance <= r
    # то выведите на консоль True, Или False, если точка лежит вовне круга.
    return is_inside


if __name__ == "__main__":
    run()