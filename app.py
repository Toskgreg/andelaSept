# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from tasks import Task, todo_list  # import other functions as well
from accounts import accounts, Account,ACCOUNTS # import the function as well


if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """
    name = input("Enter your name: ")
    password  = input("Enter your password: ")

    """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g 
    """
    Account.add_account(name, password)


    """
        Provide options:
            1. creating a task
            2. deleting a task 
            3. deleting all tasks
            4. Marking a task finished

        E.g
    """

    print("Select Option:")
    print("1: Create Task")
    print("2: Delete Task")
    print("3: Delete all Tasks")
    print("4: Mark Task")
# ..... skipped code
    selection = input("selection: ")

#Write code that implements the selected option
    if selection == "1":
        task=input("add ur todo: ")
        Task.create_task(task)
        save_data = task 
        data = open('data.txt', 'a')
        data.write(save_data)
        data.close()
        print ("Your todo has been successfully saved.")
        print (todo_list)

    if selection == "2":
        task_id=input("add ur taskid: ")
        Task.delete_task(task_id)
        print ("Your todo has been successfully deleted.")

    if selection == "3":
        Task.delete_all_tasks()
        print ("Your todolist is now empty")

    if selection == "4":
        status=input("mark ur task: ")
        Task.mark_as_finished(status)
        print ("Your todo has been successfully marked.")
        print (todo_list)
    
