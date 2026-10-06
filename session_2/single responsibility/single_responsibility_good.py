def calculate_total(sales):
    return sum(sale["amount"] for sale in sales)


def format_report(sales, total):
    report = f"Total Sales: ${total}\n"

    for sale in sales:
        report += f"{sale['product']}: ${sale['amount']}\n"

    return report


def save_report(report, filename):
    with open(filename, "w") as file:
        file.write(report)


def generate_report(sales):
    total = calculate_total(sales)
    report = format_report(sales, total)

    save_report(report, "report.txt")

    return report