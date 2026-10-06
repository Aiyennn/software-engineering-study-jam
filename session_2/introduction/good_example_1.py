tasks = []


def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def add_task():
    task = input("Enter task description: ")

    if task == "":
        print("Task cannot be empty!")
        return

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")

    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")


def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks()

    choice = input("Enter task number to remove: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    number = int(choice)

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(number - 1)
    print("Removed task:", removed_task)


def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please select between 1 and 4.")


main()