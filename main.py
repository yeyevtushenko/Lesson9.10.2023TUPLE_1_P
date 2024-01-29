def find_min_max(numbers_tuple):
    if not numbers_tuple:
        return None

    minn = min(numbers_tuple)
    maxx = max(numbers_tuple)

    return minn, maxx


numbers = (5, 3, 9, 1, 7, 2, 8)
result = find_min_max(numbers)

print(f"Найменший та найбільший елементи кортежу {numbers}: {result}")
