# This module deletes the task from txt file by using remove method of list and then writes the tasks again to txt file.
from process import process_task
from write import write_tasks

def delete_task(task):

    confirm = input('Are you sure you want to delete this task? (y/n) ')
    try:
        if confirm == 'y':
         # Delete task from storage
          tasks = process_task()
          tasks.remove(task)
          write_tasks(tasks)
          print('Task deleted')
        else:
            print('Task not deleted')
    except ValueError:
        ("Plesase enter a correct value")
  

