"""
1) Use meaningful names for variables and functions
2) Keep the control flow clear and easy to follow
3) Keep functions at a reasonable size
4) Avoid unnecessary complexity that makes the code harder to understand
5) Write comments if they provide useful context
"""

students = [
    {"id": 1001, "name": "Ana", "quiz": 85, "assignment": 90, "exam": 88},
    {"id": 1002, "name": "Ben", "quiz": 72, "assignment": 68, "exam": 75},
    {"id": 1003, "name": "Carla", "quiz": 95, "assignment": 92, "exam": 96},
    {"id": 1004, "name": "David", "quiz": 60, "assignment": 65, "exam": 58},
]

def get(a, b):
    x = []
    for i in a:
        if b.lower() in i["name"].lower():
            x.append(i)
    return x

def calc(a):
    return (a["quiz"] * .2) + (a["assignment"] * .3) + (a["exam"] * .5)


def show(a):
    for i in a:
        x = calc(i)
        if x >= 75:
            y = "PASSED"
        else:
            y = "FAILED"

        print(
            i["name"],
            " | Grade:", round(x, 2),
            " |", y
        )


def main():
    a = input("Enter student name: ")

    if a != "":
        b = get(students, a)

        if len(b) == 0:
            print("Student not found")
        else:
            show(b)
    else:
        print("Please enter a name")


main()