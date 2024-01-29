cities_set1 = {"Kyiv", "Lviv", "Odessa", "Kharkiv"}
cities_set2 = {"Lviv", "Dnipro", "Odessa", "Kherson"}

unique_cities_set = cities_set2.difference(cities_set1)

print("Міста, які є в другій множині, але відсутні в першій:", unique_cities_set)