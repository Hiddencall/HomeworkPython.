def is_year_leap(year):
    return True if year % 4 == 0 else False


year = int(input("Введите год: "))  # Для удобства год вводится пользователем.
yearbool = is_year_leap(year)
print(f"Год {year}: {yearbool}.")
