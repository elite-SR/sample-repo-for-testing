clear
o_list.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')
    else:
        print("No tasks yet!")

def main():
    while True:
        print("\nOptions: 1. Add Task  2. View Tasks  3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
