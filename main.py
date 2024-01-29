cities_set1 = {"Kyiv", "Lviv", "Odessa", "Kharkiv"}
cities_set2 = {"Lviv", "Dnipro", "Odessa", "Kherson"}

unique_cities_set = cities_set1.difference(cities_set2)

print("Міста, які є в першій множині, але відсутні у другій:", unique_cities_set)