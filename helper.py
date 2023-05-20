# when to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_integer():
        """
        This should do something that has a relationship
        with the class, bus not something that must be unique
        per instance!
        """
        pass

    @classmethod
    def instantiate_from_csv(cls):
        pass
        