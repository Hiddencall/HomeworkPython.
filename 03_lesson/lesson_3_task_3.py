from address import Address
from mailing import Mailing

to_address = Address("392 321", "Тамбов", "ул.Интернациональная", "36", "214")
from_address = Address("453 234", "Москва", "ул.Невзорова", "6", "13")
cost = "500"
track = '"Заказное письмо"'

mailing = Mailing(to_address, from_address, cost, track)
print(mailing)
