


manager = TaskManager()
manager.load_from_file()

while True:
    print("\n===== Student Task Tracker =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        title = input("Title: ")
        desc = input("Description: ")
        manager.add_task(title, desc)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        id = int(input("Task ID: "))
        title = input("New Title: ")
        desc = input("New Description: ")
        manager.update_task(id, title, desc)

    elif choice == "4":
        id = int(input("Task ID: "))
        manager.delete_task(id)

    elif choice == "5":
        id = int(input("Task ID: "))
        manager.search_task(id)

    elif choice == "6":
        manager.save_to_file()
        print("Exiting...")
        break

    else:
        print("Invalid option!")