def replace_manufacturer(tuple_of_manufacturers, target_manufacturer, replacement_word):
    replaced_tuple = tuple(replacement_word if manufacturer == target_manufacturer else manufacturer
                           for manufacturer in tuple_of_manufacturers)
    return replaced_tuple


manufacturers = ("Toyota", "Ford", "Honda", "Toyota", "Nissan", "Chevrolet", "Toyota", "Subaru")

target = input("Введіть назву автовиробника для заміни: ")
word = input("Введіть слово для заміни: ")

result = replace_manufacturer(manufacturers, target, word)

print(f"Оновлений кортеж: {result}")