from models.shipping import ShippingService
def checkout(customer, cart):
    if cart.is_empty():
        raise ValueError("Cart is empty.")

    subtotal = 0
    shipping_items = []

    for item in cart.get_items():
        product = item.product
        qty = item.quantity

        if product.is_expired():
            raise ValueError(f"{product.name} is expired.")
        if qty > product.quantity:
            raise ValueError(f"Not enough stock for {product.name}")
        
        product.quantity -= qty
        subtotal += product.price * qty

        if product.is_shippable():
            for _ in range(qty):
                shipping_items.append(product)

    shipping_fee = 30 if shipping_items else 0
    total_amount = subtotal + shipping_fee

    customer.deduct_balance(total_amount)

    if shipping_items:
        ShippingService().ship(shipping_items)

    print("** Checkout receipt **")
    for item in cart.get_items():
        total = item.product.price * item.quantity
        print(f"{item.quantity}x {item.product.name}\t{total}")
    print("-" * 22)
    print(f"Subtotal\t{subtotal}")
    print(f"Shipping\t{shipping_fee}")
    print(f"Amount\t\t{total_amount}")
    print(f"Remaining Balance: {customer.balance}\n")
