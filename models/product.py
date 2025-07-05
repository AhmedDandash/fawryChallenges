from abc import ABC, abstractmethod
from datetime import date

class Product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def is_expired(self) -> bool:
        pass

    @abstractmethod
    def is_shippable(self) -> bool:
        pass


class ExpirableShippableProduct(Product):
    def __init__(self, name, price, quantity, weight, expiry_date: date):
        super().__init__(name, price, quantity)
        self.weight = weight  
        self.expiry_date = expiry_date

    def is_expired(self):
        return date.today() > self.expiry_date

    def is_shippable(self):
        return True

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight
class ShippableProduct(Product):
    def __init__(self, name, price, quantity, weight):
        super().__init__(name, price, quantity)
        self.weight = weight 

    def is_expired(self):
        return False

    def is_shippable(self):
        return True

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight
class NonShippableProduct(Product):
    def is_expired(self):
        return False

    def is_shippable(self):
        return False
