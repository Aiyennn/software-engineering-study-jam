from datetime import datetime

# TASK: Implement a product search feature.
# Users should be able to search for products by name or category.
# Display all matching products in the search results.

# ============================================================
# DATA
# ============================================================

products = [
    {
        "id": 101,
        "name": "Mechanical Keyboard",
        "category": "Accessories",
        "price": 3500,
        "stock": 12
    },
    {
        "id": 102,
        "name": "Wireless Mouse",
        "category": "Accessories",
        "price": 1500,
        "stock": 25
    },
    {
        "id": 103,
        "name": "USB-C Hub",
        "category": "Accessories",
        "price": 2200,
        "stock": 8
    },
    {
        "id": 104,
        "name": "Laptop Stand",
        "category": "Office",
        "price": 1800,
        "stock": 15
    },
    {
        "id": 105,
        "name": "27-inch Monitor",
        "category": "Monitors",
        "price": 14500,
        "stock": 6
    },
    {
        "id": 106,
        "name": "Webcam",
        "category": "Accessories",
        "price": 2800,
        "stock": 10
    }
]

cart = []

orders = []


# ============================================================
# PRODUCT FUNCTIONS
# ============================================================

def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None


def display_product(product):
    print(
        f"{product['id']} | "
        f"{product['name']} | "
        f"{product['category']} | "
        f"₱{product['price']:,} | "
        f"Stock: {product['stock']}"
    )


def list_products():
    print("\n--- PRODUCT CATALOG ---")

    for product in products:
        display_product(product)


# ============================================================
# CART FUNCTIONS
# ============================================================

def add_to_cart(product_id, quantity):
    product = find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    if product["stock"] < quantity:
        print("Not enough stock.")
        return

    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            print("Cart updated.")
            return

    cart.append({
        "product_id": product_id,
        "quantity": quantity
    })

    print(f"{product['name']} added to cart.")


def remove_from_cart(product_id):
    for item in cart:
        if item["product_id"] == product_id:
            cart.remove(item)
            print("Item removed from cart.")
            return

    print("Item not found in cart.")


def view_cart():
    print("\n--- YOUR CART ---")

    if not cart:
        print("Cart is empty.")
        return

    total = 0

    for item in cart:
        product = find_product(item["product_id"])

        subtotal = product["price"] * item["quantity"]
        total += subtotal

        print(
            f"{product['name']} | "
            f"Qty: {item['quantity']} | "
            f"₱{subtotal:,}"
        )

    print(f"\nTotal: ₱{total:,}")


# ============================================================
# CHECKOUT
# ============================================================

def checkout():
    if not cart:
        print("Cart is empty.")
        return

    total = 0

    for item in cart:
        product = find_product(item["product_id"])

        if product["stock"] < item["quantity"]:
            print(f"Not enough stock for {product['name']}.")
            return

        total += product["price"] * item["quantity"]

    for item in cart:
        product = find_product(item["product_id"])
        product["stock"] -= item["quantity"]

    order = {
        "id": len(orders) + 1,
        "items": cart.copy(),
        "total": total,
        "date": datetime.now()
    }

    orders.append(order)
    cart.clear()

    print("\nOrder placed successfully!")
    print(f"Order ID: {order['id']}")
    print(f"Total: ₱{total:,}")


# ============================================================
# ORDER HISTORY
# ============================================================

def view_orders():
    print("\n--- ORDER HISTORY ---")

    if not orders:
        print("No orders yet.")
        return

    for order in orders:
        print(
            f"Order #{order['id']} | "
            f"₱{order['total']:,} | "
            f"{order['date'].strftime('%Y-%m-%d %H:%M')}"
        )


# ============================================================
# ADMIN FUNCTIONS
# ============================================================

def restock_product(product_id, quantity):
    product = find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    product["stock"] += quantity

    print(
        f"{product['name']} restocked. "
        f"New stock: {product['stock']}"
    )


# ============================================================
# APPLICATION
# ============================================================

def main():
    while True:

        print("\n==============================")
        print("       ONLINE STORE")
        print("==============================")

        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Order History")
        print("7. Restock Product")
        print("8. Search Prouct")
        print("9. Exit")

        choice = input("\nChoose an option: ")

        match choice:
            case "1":
                list_products()

            case "2":
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity: "))

                add_to_cart(product_id, quantity)

            case "3":
                product_id = int(input("Product ID: "))

                remove_from_cart(product_id)

            case "4":
                view_cart()

            case "5":
                checkout()

            case "6":
                view_orders()

            case "7":
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity: "))

                restock_product(product_id, quantity)

            case "8":
                print("Goodbye!")
                break

            case _:
                print("Invalid option.")


if __name__ == "__main__":
    main()