from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f'Broken phone {broken_phones} must be greater than or equal to zero!'

        self.broken_phones = broken_phones
