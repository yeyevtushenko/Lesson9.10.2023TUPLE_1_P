def remove_common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common_characters = set1.intersection(set2)

    result_str1 = ''.join(char for char in str1 if char not in common_characters)
    result_str2 = ''.join(char for char in str2 if char not in common_characters)

    return result_str1, result_str2


string1 = "hello"
string2 = "world"
result1, result2 = remove_common_characters(string1, string2)
print(f"Рядок 1 без спільних літер: {result1}")
print(f"Рядок 2 без спільних літер: {result2}")