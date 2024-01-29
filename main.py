countries = set()

def add_country(country):
    countries.add(country)
    print(f"{country} додано до множини.")

def remove_country(country):
    if country in countries:
        countries.remove(country)
        print(f"{country} видалено з множини.")
    else:
        print(f"{country} не знайдено в множині.")

def search_country(query):
    matching_countries = [country for country in countries if query.lower() in country.lower()]
    if matching_countries:
        print(f"Знайдені країни, які містять '{query}': {', '.join(matching_countries)}")
    else:
        print(f"Країни, які містять '{query}', не знайдено.")

def check_country_existence(country):
    if country in countries:
        print(f"{country} знаходиться в множині.")
    else:
        print(f"{country} не знайдено в множині.")

while True:
    print("\nОберіть опцію:")
    print("1. Додати країну")
    print("2. Видалити країну")
    print("3. Пошук країн")
    print("4. Перевірити наявність країни")
    print("0. Завершити програму")

    choice = input("Ваш вибір: ")

    if choice == "1":
        country = input("Введіть назву країни, яку хочете додати: ")
        add_country(country)
    elif choice == "2":
        country = input("Введіть назву країни, яку хочете видалити: ")
        remove_country(country)
    elif choice == "3":
        query = input("Введіть символи для пошуку країн: ")
        search_country(query)
    elif choice == "4":
        country = input("Введіть назву країни для перевірки наявності: ")
        check_country_existence(country)
    elif choice == "0":
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
