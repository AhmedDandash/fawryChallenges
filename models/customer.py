class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deduct_balance(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
