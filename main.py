from datetime import date
from models.product import ExpirableShippableProduct, ShippableProduct, NonShippableProduct
from models.customer import Customer
from models.cart import Cart
from models.checkout import checkout

def main():
    cheese = ExpirableShippableProduct("Cheese", 100, 10, 200, date(2025, 12, 1)) 
    biscuits = ExpirableShippableProduct("Biscuits", 150, 10, 700, date(2025, 10, 1))
    tv = ShippableProduct("TV", 3000, 5, 10000)
    scratch_card = NonShippableProduct("Scratch Card", 50, 20)

    ahmed = Customer("Ahmed", 4000)
    cart = Cart()
    cart.add(cheese, 2)
    cart.add(biscuits, 1)
    cart.add(scratch_card, 1)
    cart.add(tv, 1)

    checkout(ahmed, cart)

if __name__ == "__main__":
    main()
