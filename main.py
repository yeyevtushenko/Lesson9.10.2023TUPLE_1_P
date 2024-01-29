cities_set1 = {'Kyiv', 'Odessa', 'Kharkiv', 'Lviv', 'Dnipro'}
cities_set2 = {'Kharkiv', 'Kherson', 'Lviv', 'Dnipro'}

unique_cities_set1 = cities_set1 - cities_set2
unique_cities_set2 = cities_set2 - cities_set1

result_set = unique_cities_set1.symmetric_difference(unique_cities_set2)

for city in result_set:
    if city in unique_cities_set1:
        print(f"{city} - унікальний для множини cities_set1")
    else:
        print(f"{city} - унікальний для множини cities_set2")
