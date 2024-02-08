# This is the main function.
# username is todoapp
# password is 123@todo

from pendingtask import view_pending_task
from create import create_new_task
from viewlist import view_list
from login import check_login


def main_menu():
    check_login("todoapp", "123@todo")
    while True:
        print("Todo List Application\n")
        print("1. View all tasks")
        print("2. View pending tasks")
        print("3. Create a new task")
        print("4. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_list()
        elif choice == "2":
            view_pending_task()
        elif choice == "3":
            create_new_task()
        elif choice == "4":
            print("See ya!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main_menu()
