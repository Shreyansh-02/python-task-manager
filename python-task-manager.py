
filename = "tasks.txt"
try:
    with open(filename, "r") as file:
        tasks = file.readlines()
except FileNotFoundError:
    print("No file found. Creating new task list.")
    tasks = []

def save_tasks():
    with open(filename, "w") as file:
        file.writelines(tasks)

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(str(count) + ". " + task.strip())
                count += 1

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task + "\n")
        save_tasks()
        print("Task added!")

    elif choice == "3":
        try:
            number = int(input("Enter task number to edit: "))
            if 1 <= number <= len(tasks):
                new_text = input("Enter new task text: ")
                tasks[number - 1] = new_text + "\n"
                save_tasks()
                print("Task updated!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                save_tasks()
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
 
