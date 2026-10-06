students = [
    {"id": 1001, "name": "Ana", "quiz": 85, "assignment": 90, "exam": 88},
    {"id": 1002, "name": "Ben", "quiz": 72, "assignment": 68, "exam": 75},
    {"id": 1003, "name": "Carla", "quiz": 95, "assignment": 92, "exam": 96},
    {"id": 1004, "name": "David", "quiz": 60, "assignment": 65, "exam": 58},
]

# Searches for students whose names match the given search term.
def find_students(students, student_name):
    matching_students = []

    for student in students:
        if student_name.lower() in student["name"].lower():
            matching_students.append(student)

    return matching_students

# Calculates a student's final grade using the quiz, assignment, and exam weights.
def calculate_final_grade(student):
    return (
        student["quiz"] * 0.2
        + student["assignment"] * 0.3
        + student["exam"] * 0.5
    )

# Displays each student's final grade and whether they passed or failed.
def display_student_results(students):
    for student in students:
        final_grade = calculate_final_grade(student)

        if final_grade >= 75:
            status = "PASSED"
        else:
            status = "FAILED"

        print(
            student["name"],
            "| Grade:", round(final_grade, 2),
            "|", status
        )


def main():
    student_name = input("Enter student name: ")

    if not student_name:
        print("Please enter a name")
        return

    matching_students = find_students(students, student_name)

    if not matching_students:
        print("Student not found")
        return

    display_student_results(matching_students)


main()