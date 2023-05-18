import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        # assert price and quantity's values are greater than or equal to zero
        assert price>=0, f'Price {price} must be greater than or equal to zero!'
        assert quantity>=0, f'Quantity {quantity} must be greater than or equal to zero!'

        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    # define a calculation of the price and quantity
    def calculate_total_price(self):
        return self.prices * self.quantity
        
    #define a representation of items
    def __repr__(self):
        return f'Item ({self.name}, {self.price}, {self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(number):
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number,int):
            return True
        else:
            return False

    def apply_discount(self):
        self.price = self.price * self.pay_rate

# item1 = Item('MyItem', 500, 5)
# item1.apply_discount()

# print(Item.all)
print(Item.is_integer(7.3))