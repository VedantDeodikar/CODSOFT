todo_list = []
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task '" + task + "' added to your To-Do list.")
    elif choice == '2':  
        if todo_list:
            print("\nYour To-Do List:")
            for idx, task in enumerate(todo_list, 1):
                print(str(idx) + ". " + task)
        else:
            print("Your to-do list is empty.")
    elif choice == '3':  
        if todo_list:
            task_num = input("Enter the task number to delete: ")
            valid_number = True
            for char in task_num:
                if char < '0' or char > '9':  
                    valid_number = False
                    break
            if valid_number:
                task_num = int(task_num)
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print("Task '" + removed_task + "' deleted.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")
        else:
            print("Your to-do list is empty.")
    
    elif choice == '4':  
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice! Please select an option between 1 and 4.")
