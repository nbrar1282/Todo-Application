# This module is used to read from the text file and then it stores the data in the list of dictionaries and
#  returns it to use it in other functions. 

def process_task():
    all_tasks = []
    try:
        with open('task.txt', 'r') as fp:
            reader = fp.read().strip().split('\n\n')
            for read in reader:
                dictread = read.strip().split('\n')
                
                if len(dictread) == 2:
                    deadline = dictread[1]
                    
                    task = {
                        'title': dictread[0],
                        'deadline': deadline
                    }
                    all_tasks.append(task)
                elif len(dictread) > 2:
                    deadline = dictread[-1]
                    description = '\n'.join(dictread[1:-1])
                    
                    task = {
                        'title': dictread[0],
                        'deadline': deadline,
                        'description': description.strip()
                    }
                    all_tasks.append(task)

    except FileNotFoundError:
        print('You have no tasks at this time')
        
   
    return all_tasks
