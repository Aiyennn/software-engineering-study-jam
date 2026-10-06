def calculate_regular_order(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.12
    shipping = 100

    return subtotal + tax + shipping


def calculate_vip_order(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.12
    shipping = 50

    return subtotal + tax + shipping