import csv


class Item:
    def __init__(self,name:str,price:float,quantity=0):
        # assert price and quantity's values are greater than or equal to zero
        assert price>=0, f'Price {price} must be greater than or equal to zero!'
        assert quantity>=0, f'Quantity {quantity} must be greater than or equal to zero!'

        self.name = name
        self.price = price
        self.quantity = quantity
        

item1 = Item('MyItem', 500)
print(item1.name)