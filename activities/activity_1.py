# TASK: Implement a student search feature.
# Users should be able to search for students by name or course.
# Display all matching students in the search results.
# Save the file activity_1_firstname_lastname

# ============================================================
# DATA
# ============================================================

students = [
    {
        "id": 101,
        "name": "Alice Santos",
        "course": "Computer Science",
        "year": 2,
        "grade": 91
    },
    {
        "id": 102,
        "name": "Brian Cruz",
        "course": "Information Technology",
        "year": 3,
        "grade": 87
    },
    {
        "id": 103,
        "name": "Carla Reyes",
        "course": "Computer Science",
        "year": 1,
        "grade": 95
    },
    {
        "id": 104,
        "name": "Daniel Garcia",
        "course": "Business Administration",
        "year": 4,
        "grade": 82
    },
    {
        "id": 105,
        "name": "Emma Flores",
        "course": "Information Technology",
        "year": 2,
        "grade": 89
    },
    {
        "id": 106,
        "name": "Frank Mendoza",
        "course": "Computer Science",
        "year": 3,
        "grade": 93
    }
]


# ============================================================
# STUDENT FUNCTIONS
# ============================================================

def display_student(student):
    print(
        f"{student['id']} | "
        f"{student['name']} | "
        f"{student['course']} | "
        f"Year {student['year']} | "
        f"Grade: {student['grade']}"
    )


def list_students():
    print("\n--- STUDENT LIST ---")

    for student in students:
        display_student(student)


def search_student():
    pass


# ============================================================
# APPLICATION
# ============================================================

def main():
    while True:

        print("\n==============================")
        print("       STUDENT SYSTEM")
        print("==============================")

        print("1. View Students")
        print("2. Search Students")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        match choice:
            case "1":
                list_students()

            case "2":
                search_student()

            case "3":
                print("Goodbye!")
                break

            case _:
                print("Invalid option.")


if __name__ == "__main__":
    main()