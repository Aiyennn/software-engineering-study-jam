def generate_report(sales):
    # Calculate total
    total = sum(sale["amount"] for sale in sales)

    # Format report
    report = f"Total Sales: ${total}\n"

    for sale in sales:
        report += f"{sale['product']}: ${sale['amount']}\n"

    # Save report
    with open("report.txt", "w") as file:
        file.write(report)

    # Send report
    print("Sending report to manager...")

    return report