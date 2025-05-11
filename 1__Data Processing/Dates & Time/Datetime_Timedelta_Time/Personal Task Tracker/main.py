from task_manager import TaskManager
from utils import parse

def main():
    manager = TaskManager()

    while True:
        print("\nPersonal Task Tracker")
        print("1. ADD A TAST")
        print("2. SHOW ALL TASKS")
        print("3. DELETE TASK")
        print("4. EXIT")

        choice = input("CHOOSE U`RE ACTION: ")

        if choice == "1":
            title = input("ENTER A NAME OF THE TASK: ")
            due_date_str = input("ENTER A TIME LIMIT (year-month-day): ")

            due_date = parse(due_date_str)
            if due_date:
                manager.add_task(title, due_date)
                print("TASK HAS BEEN UPDATED.")
            else:
                print("WRONG DATE FORMAT.")

        elif choice == "2":
            manager.display_tasks()

        elif choice == "3":
            task_id = input("ENTER ID FOR DELETING: ")
            try:
                manager.remove_task(int(task_id))
                print("TASK HAS BEEN DELETED.")
            except ValueError:
                print("WRONG ID.")

        elif choice == "4":
            print("EXIT FROM THE SISTEM.")
            break

        else:
            print("WRONG CHOICE. TRY AGAIN")

if __name__ == "__main__":
    main()