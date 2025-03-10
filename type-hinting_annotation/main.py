from typing import List, Dict

class Task:
    def __init__(self, title: str, priority: int = 1) -> None:
        self.title: str = title
        self.priority: int = priority
        self.completed: bool = False
    
    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        status: str = "✔ Done" if self.completed else "❌ Not done"
        return f"Task: {self.title} | Priority: {self.priority} | Status: {status}"

class ToDoList:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, title: str, priority: int = 1) -> None:
        new_task: Task = Task(title, priority)
        self.tasks.append(new_task)
        print(f"Added: {title}")

    def show_tasks(self) -> None:
        if not self.tasks:
            print("No tasks yet!")
        for task in self.tasks:
            print(task)

    def complete_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task '{self.tasks[index].title}' marked as done.")
        else:
            print("Invalid task number!")

def main() -> None:
    todo = ToDoList()
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Complete task\n4. Exit")
        choice: str = input("Choose an option: ")

        if choice == "1":
            title: str = input("Enter task title: ")
            priority: int = int(input("Enter priority (1-5): "))
            todo.add_task(title, priority)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            index: int = int(input("Enter task number to complete: "))
            todo.complete_task(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
