from datetime import datetime, timedelta
class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def __str__(self):
        return f"{self.title} (UNTIL {self.due_date.strftime('%Y-%m-%d')})"

class TaskManager: 
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, due_date):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = Task(title, due_date)
    def display_tasks(self):
        if not self.tasks:
            print("A LIST OF THE TASKS IS EMPTY.")
        else:
            for task_id, task in self.tasks.items():
                print(f"{task_id}: {task}")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            print("A TASK WITH THIS ID WASN`T FOUNF.")