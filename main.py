def intro():
    print("Welcome to the To-Do List App")
    print("I'm here to help you manage your tasks.")
    print("-" * 44)
    print("|  Enter the number to perform a task:     |")
    print("|  1 - Add Task(s)                         |")
    print("|  2 - Remove Task(s)                      |")
    print("|  3 - Display Task(s)                     |")
    print("|  4 - Completed Task(s)                   |")
    print("|  5 - Edit Task(s)                        |")
    print("|  Q - Quit the program                    |")
    print("-" * 44)



def add_task(tasks): #Function that add each task from user to the list
    while True:
        items = input("Enter your task or 'Q' when done entering task(s): ")
        if items == "Q" or items =="q":
            break
        else:
            tasks.append(items)
    return tasks

def remove_task(tasks): # remove task user do not want in the list
    while True:
        items = input("Enter the task you want removed or 'Q' when done: ")
        if items == "Q" or items == "q":
            break
        # elif items != tasks(items)
        else:
            if items in tasks:
                tasks.remove(items)
                print(f"{items} was removed.")
            else:
                print(f"{items} not found in your To Do List, please enter a valid item(s) ")
    return tasks

def display_task(tasks): #Display the task list to user
    count = 1
    for i in tasks:
        print(f"{count} - {i}")
        count += 1
    input("Press Enter to Continue...")
    return tasks



def edit_tasks(tasks):
    while True:
        edit_task = input("Enter the task you will like to change or 'Q' to quit ")
        if edit_task  == "Q" or edit_task == "q":
            break
        elif edit_task in tasks:
            index = tasks.index(edit_task)
            new_task = input(f"Enter the new task for {edit_task} ")
            tasks[index] = new_task
            print(f"Task {edit_task} has been updated to {new_task} ")
        else:
            print(f"{edit_task} not found in your To-Do List. Please enter a valid Task. ")









# tasks =["walk the dogs", "do laundry", "go to the doctors"]
# display_task(tasks)

#
# tasks =[]
# add_task(tasks)
# print(tasks)




tasks = []
while True:
    intro()

    choice = input("Enter the one of options(1-5) or 'Q' to quit program: ")
    if choice == "Q" or choice == "q":
        print("Are you sure you want to exit the To-Do-List App? ")
        choice = input("Enter 'Y' to quit app or 'N' to continue using the app ")
        choice = choice.lower()
        if choice == "y":
            print("Thank you for using the To-Do List App. Enjoy your day!")
            quit()
        elif choice == "n":
            print("Great! Continue managing your tasks.")
            continue
        else:
            print("Invalid input. Please type  'Y or 'N'")
    elif choice == "1":
        add_task(tasks)
    elif choice == "2":
        remove_task(tasks)
    elif choice == "3":
        display_task(tasks)
    elif choice == "4":
        completed_task(tasks)
    elif choice == "5":
        edit_tasks(tasks)
    else:
        print("Please enter a valid choice(1-5) or Q")
        continue
