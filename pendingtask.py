''' This module has two functions view pending task and option task. View pending task function shows the tasks which have deadline in future 
in ascending order
whereas option task function performs various function on the selected function.'''

from datetime import datetime
from process import process_task  # importing local module
from view import view_task  # importing local module
from delete import delete_task  # importing local module

def view_pending_task():
    """View and interact with pending tasks sorted by date."""

    tasks = process_task()   # Retrieve all tasks
    all_tasks = sorted(tasks, key=lambda x: datetime.strptime(x['deadline'], '%d %B %Y'))  # Sort tasks by deadline date
    deadline_tasks = []   # List to store all pending tasks
    today = datetime.now()   # Get current date and time
    i = 0   

    for task in all_tasks:
        deadline = task['deadline']
        date_deadline = datetime.strptime(deadline, '%d %B %Y')   # Convert deadline date string to datetime object
        if date_deadline > today:   # Check if task is pending
            print(i+1, ' Title:', task['title'])   
            i += 1   # Increment counter for pending tasks
            deadline_tasks.append(task)  

    if i > 0:
        while True:
            try:
                select_task = int(input('Enter the number of the task you want to select or press 0 to go back to main menu: '))
                if select_task == 0:
                    return
                elif select_task > 0:
                    selected_task = deadline_tasks[int(select_task) - 1]   # Select the pending task that the user wants to view or delete
                    print('Selected task:', selected_task['title'])
                    break
            except (ValueError, IndexError):
                print("Error: Invalid input. Please enter a number from 1 to", i, "or press 0 to go back to main menu.")
        optiontask(selected_task)   # Call the optiontask() function to perform an action on the selected task
    else:
        print("Sorry you don't have any tasks right now")

def optiontask(task):
    """Perform an action on the selected task."""

    while True:
        action = input('What would you like to do with this task? (view/delete/back) ')
        if action == 'view':
            view_task(task)   # Call the view_task() function to display details of the selected task
            while True:
                ask = input('Press b to go back to task list')
                if ask == 'b':
                    return view_pending_task()   
                else:
                    print('invalid entry')

        elif action == 'delete':
            delete_task(task)   # Call the delete_task() function to delete the selected task
            while True:
                ask = input('Press b to go back to task list')
                if ask == 'b':
                    return view_pending_task()   
                else:
                    print('invalid entry')

        elif action == 'back':
            return view_pending_task()  
        else:
            print('Invalid action')   # Print error message for invalid input action
