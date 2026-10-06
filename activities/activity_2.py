# ============================================================
# HANDS-ON SESSION: CODE QUALITY PRINCIPLES
# ============================================================
#
# You will practice three principles:
#
# 1. Readability
# 2. Single Responsibility Principle (SRP)
# 3. Don't Repeat Yourself (DRY)
#
# IMPORTANT:
# - Read the comments for your instructions.
# - Save the file activity_2_firstname_lastname
# ============================================================


# ============================================================
# 1. READABILITY
# ============================================================
#
# TASK:
# Rewrite the function below to make it easier to understand.
#
# Your goal is NOT to change what the program does.
#
# Improve the code by:
# - Using meaningful variable names
# - Breaking complicated expressions into understandable steps
# - Using clear function and parameter names
# - Removing unnecessary code
#
# Expected behavior:
# - Calculate the total price of the items
# - Apply a 10% discount if the total is greater than 1000
# - Return the final price
#
# Do NOT change the expected result. | You can modify the code however you want
# ============================================================

def calc(x):
    a = sum(i["p"] * i["q"] for i in x)

    if a > 1000:
        a = a - (a * 0.10)

    return a


items = [
    {"p": 500, "q": 2},
    {"p": 200, "q": 1},
    {"p": 100, "q": 3}
]

print(calc(items))

# ============================================================
# 2. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ============================================================
#
# TASK:
# Refactor the function below using the
# Single Responsibility Principle.
#
# The current function is responsible for TOO MANY things:
# - Calculating the total
# - Creating the report
# - Saving the report to a file
#
# Your job:
# - Separate these responsibilities into different functions.
# - Each function should have ONE clear responsibility.
#
# The final program should still:
# 1. Calculate the total sales
# 2. Create the report
# 3. Save the report to "sales_report.txt"
# You can modify the code however you want
# ============================================================

def generate_report(sales):
    # Calculate total
    total = sum(sale["amount"] for sale in sales)

    # Format report
    report = f"Total Sales: ${total}\n"

    for sale in sales:
        report += f"{sale['product']}: ${sale['amount']}\n"

    # Save report
    with open("sales_report.txt", "w") as file:
        file.write(report)


sales = [
    {"product": "Laptop", "amount": 50000},
    {"product": "Mouse", "amount": 1000},
    {"product": "Keyboard", "amount": 2500}
]

generate_report(sales)

# ============================================================
# 3. DON'T REPEAT YOURSELF (DRY)
# ============================================================
#
# TASK:
# Refactor the code below so that the repeated logic
# only exists in ONE place.
#
# Look carefully at the three functions.
#
# You will notice that they all:
# - Calculate the subtotal
# - Calculate the tax
# - Add the tax to the subtotal
#
# Your job:
# - Identify the repeated code.
# - Create a reusable function for the repeated logic.
# - Use that function inside the existing functions.
#
# The functions should still produce the same results.
#
# You can modify the code however you want
# ============================================================

def calculate_food_total(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.12
    total = subtotal + tax
    return total


def calculate_clothing_total(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.12
    total = subtotal + tax
    return total


def calculate_electronics_total(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.12
    total = subtotal + tax
    return total


print(calculate_food_total(500, 2))
print(calculate_clothing_total(1000, 3))
print(calculate_electronics_total(5000, 1))