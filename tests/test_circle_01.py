from circle_01 import area, point, compute


def test_area_radius_42():
    assert area(42) == 5541.7693


def test_area_radius_1():
    assert area(1) == 3.1416


def test_point_inside():
    assert point(42, (23, 34)) is True


def test_point_outside():
    # sqrt(30**2 + 30**2) ≈ 42.43 > 42
    assert point(42, (30, 30)) is False


def test_point_on_border():
    # (3, 4) лежит ровно на окружности радиуса 5
    assert point(5, (3, 4)) is True


def test_compute_wrapper():
    # compute подставляет фиксированный radius=42
    assert compute(area, None) == 5541.7693
    assert compute(point, (23, 34)) is True