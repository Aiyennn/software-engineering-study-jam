def generate_receipt(order):
    # Calculate total
    subtotal = sum(
        item["price"] * item["quantity"]
        for item in order["items"]
    )

    tax = subtotal * 0.12
    total = subtotal + tax

    # Format invoice
    invoice = f"""
    Invoice
    ----------------
    Customer: {order["customer"]}

    Subtotal: ${subtotal:.2f}
    Tax:      ${tax:.2f}
    Total:    ${total:.2f}
    """

    # Save invoice
    with open("invoice.txt", "w") as file:
        file.write(invoice)

    # Send invoice
    print(f"Sending invoice to {order['email']}...")

    return invoice