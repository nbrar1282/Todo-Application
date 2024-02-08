# This module writes the task to the task.txt file sorted according to date.
from datetime import datetime
def write_tasks(tasks) : 
    all_tasks = sorted(tasks, key=lambda x: datetime.strptime(x['deadline'], '%d %B %Y'))
 
    with open('task.txt', 'w') as file:
            for task in all_tasks:
      
                file.write(task['title'] + '\n')
                if 'description' in task:
                 file.write(task['description'] + '\n')
                file.write(task['deadline'] + '\n')
                file.write('\n')
   





        

  



















