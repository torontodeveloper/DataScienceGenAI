prompt = 'plz enter task\n'
task_list = []
while True:
    task = input(prompt)
    if task=='!':
        break
    task_list.append(task)
    
print('Here is ur task list')

for task in task_list:
    print(f'task is {task}')