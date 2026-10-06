def calculate_order_total(price, quantity, shipping):
    subtotal = price * quantity
    tax = subtotal * 0.12

    return subtotal + tax + shipping


def calculate_regular_order(price, quantity):
    return calculate_order_total(price, quantity, shipping=100)


def calculate_vip_order(price, quantity):
    return calculate_order_total(price, quantity, shipping=50)