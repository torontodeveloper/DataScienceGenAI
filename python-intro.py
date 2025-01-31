task_list = []
while True:
    task = input('plz enter ur todo tassks \n')
    if task=='!':
        break
    task_list.append(task.capitalize())
    
for task in task_list:
    print(f'{task}')