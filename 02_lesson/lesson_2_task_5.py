def month_to_season(number_month):
    if number_month == 12 or number_month < 3:
        print("Зима")
    elif number_month > 2 and number_month < 6:
        print("Весна")
    elif number_month > 5 and number_month < 9:
        print("Лето")
    elif number_month > 8 and number_month < 12:
        print("Осень")
    else:
        print("Неверный номер месяца.")


number_month = int(input("Введите номер месяца в году: "))
month_to_season(number_month)
