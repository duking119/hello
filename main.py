from item import Item
from phone import Phone

Item.instantiate_from_csv()
phone1 = Phone("jsvPhone10", 500, 5, 1)
phone2 = Phone("jsvPhone20", 700, 3, 1)

print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)
