task_list = []

while True:
    msg = input("plz enter ur task \n")
    if msg == "!":
        break
    task_list.append(msg)
print("Here are task list is \n")
for task in task_list:
    print(task)
