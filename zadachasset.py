def find_intersection(x1, x2, y1, y2) -> str:
    points_1 = []
    points_2 = []
    if x1 > x2:
        points_1 = set(range(x2, x1))
    elif x1 < x2:
        points_1 = set(range(x1, x2))
    else:
        points_1 = {x1}

    if y1 > y2:
        points_2 = set(range(y2, y1))
    elif y1 < x2:
        points_2 = set(range(y1, y2))
    else:
        points_2 = {y1}

    if points_1.intersection(points_2):
        return 'Да'
    else:
        return 'Нет'


print(find_intersection(5, 9, 6, 10))