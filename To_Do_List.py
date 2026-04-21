todolist = []

def add_task():
    task = input("Enter a task: ")
    todolist.append({"Task": task, "Status": "Pending"})
    print(" New Task Added Successfully!\n")

def view_task():
    print("\n Your ToDo List:")
    if len(todolist) == 0:
        print(" No tasks available!")
    else:
        for index, task in enumerate(todolist, 1):
            print(f"{index}. {task['Task']} - {task['Status']}")
    print()

def remove_task():
    if len(todolist) == 0:
        print(" List is Empty!")
    else:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(todolist):
                removed = todolist.pop(index)
                print(f" Task Removed: {removed['Task']}")
            else:
                print(" Invalid Task Number!")
        except ValueError:
            print(" Please enter a valid number!")

def mark_done():
    if len(todolist) == 0:
        print(" List is Empty!")
    else:
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(todolist):
                todolist[index]['Status'] = "Done"
                print(f" Task '{todolist[index]['Task']}' marked as Done!")
            else:
                print(" Invalid Task Number!")
        except ValueError:
            print(" Please enter a valid number!")

def menu():
    while True:
        print("\n*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View all Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print(" Exiting... Bye!")
            break
        else:
            print(" Invalid choice! Try again.")

menu()