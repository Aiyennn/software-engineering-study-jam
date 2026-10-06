tasks = []


def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def do_everything():
    while True:
        display_menu()
        c = input("Enter choice (1-4): ")

        if c == "1":
            t = input("Enter task description: ")
            if t != "":
                tasks.append(t)
                print("Task added successfully!")
            else:
                print("Task cannot be empty!")

        elif c == "2":
            if len(tasks) == 0:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                i = 1
                for item in tasks:
                    print(str(i) + ". " + item)
                    i = i + 1

        elif c == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                print("\nCurrent Tasks:")
                i = 1
                for item in tasks:
                    print(str(i) + ". " + item)
                    i = i + 1

                val = input("Enter task number to remove: ")
                if val.isdigit():
                    num = int(val)
                    if num >= 1 and num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print("Removed task: " + removed)
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        elif c == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 4.")


do_everything()
