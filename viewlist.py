# This module has two functions view list and perform task. View list function shows the tasks in ascending order
# whereas perform task function performs various function on the selected function.

from process import process_task
from datetime import datetime
from view import view_task
from delete import delete_task

def view_list():
    tasks = process_task()  # get all tasks
    all_tasks = sorted(tasks, key=lambda x: datetime.strptime(x['deadline'], '%d %B %Y'))  # sort tasks by deadline
    i = 0
    for task in all_tasks:
        print(i+1, ' Title:', task['title'])  # print task title
        i += 1
    if i > 0:
        while True:
            try:
                select_task = int(input('Enter the number of the task you want to select or press 0 to go back to main menu: '))
                if select_task == 0:
                    return  # return to main menu
                elif select_task > 0 and select_task <= len(tasks):
                    selected_task = tasks[select_task-1]  # select a task
                    perform_action(selected_task)  # perform an action on the selected task
                    break
                else:
                    raise IndexError('Invalid task number. Please try again.')
            except ValueError as ve:
                print(str(ve))
            except IndexError as ie:
                print(str(ie))
    else:
        print("Sorry you don't have any tasks right now")

def perform_action(selected_task):
    while True:
        try:
            action = input('What would you like to do with this task? (view/delete/back) ')
            if action == 'view':
                view_task(selected_task)  # view a task
                while True:
                    ask = input('Press b to go back to task list: ')
                    if ask == 'b':
                        return view_list()
                    else:
                        print('Invalid entry. Please try again.')
            elif action == 'delete':
                delete_task(selected_task)  # delete a task
                while True:
                    ask = input('Press b to go back to task list: ')
                    if ask == 'b':
                        return view_list()
                    else:
                        print('Invalid entry. Please try again.')
            elif action == 'back':
                return view_list()  # return to task list
            else:
                raise ValueError('Invalid input. Please try again.')
        except Exception as e:
            print(f'An error occurred: {str(e)}. Please try again.')
