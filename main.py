def count_fruits(tuple_of_fruits, target_fruit):
    count = tuple_of_fruits.count(target_fruit)
    return count


tuple = ("apple", "banana", "orange", "apple", "grape", "apple", "kiwi")

input = input("Введіть назву фрукта: ")

result = count_fruits(tuple, input)

print(f"Кількість {input} у кортежі: {result}")
