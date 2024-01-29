def count_fruits_partial(tuple_of_fruits, target_fruit):
    count = sum(target_fruit in fruit for fruit in tuple_of_fruits)
    return count


tuple = ("apple", "banana", "orange", "apple", "grape", "apple", "kiwi", "bananamango", "mango", "strawberry-banana")

input = input("Введіть назву фрукта: ")
result = count_fruits_partial(tuple, input)

print(f"Кількість {input} та його частин у кортежі: {result}")