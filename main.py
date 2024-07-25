tasks = []
def addTask():
    task = input('Please enter your task : ')
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def  deleteTask():
    listTasks()
    try:
        tasktodelete = int(input('Enter the # to delete : '))
        if tasktodelete >= 0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f'Task {tasktodelete} has been removed.')
        else:
            print(f'task #{tasktodelete} was not found.')
    except:
        print('Invalid input.')

def listTasks():
    if not tasks:
        print('There are no tasks currently')
    else:
        print('Current Task :')
        for index , task in enumerate(tasks):
            print(f'Task #{index}. {task}')

if __name__ == "__main__":
    print('Welcome to the To Do List App :')
    while True:
        print('\n')
        print('Please select one of the following options')
        print('-------------------------------------------')
        print('1 - Add a new Task')
        print('2 - Delete a Task')
        print('3 - List Task')
        print('4 - Quit')
        print('-------------------------------------------')

        choice = int(input('Enter your choice : '))
        if choice == 1 :
            addTask()

        elif choice == 2 :
            deleteTask()

        elif choice == 3 :
            listTasks()

        elif choice == 4 :
            break

        else:
            print('Invalid Options . Please Try Again ')
    print('GoodBye')

        
        
              


