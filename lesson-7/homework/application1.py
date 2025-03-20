import json
import csv
import os


# Task 1: Define the Task class
class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }


# Task 2: Define Storage Classes
class Storage:
    def save(self, tasks, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError


class JSONStorage(Storage):
    def save(self, tasks, filename="tasks1.json.json"):
        with open(filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)

    def load(self, filename="tasks1.json.json"):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return [Task(**data) for data in json.load(file)]


class CSVStorage(Storage):
    def save(self, tasks, filename="tasks1.json.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, filename="tasks1.json.csv"):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return [Task(**row) for row in reader]


# Task 3: Implement ToDoManager
class ToDoManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save(self.tasks)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title: task.title = title
                if description: task.description = description
                if due_date: task.due_date = due_date
                if status: task.status = status
                self.storage.save(self.tasks)
                return "Task updated."
        return "Task not found."

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.storage.save(self.tasks)

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]


# Task 4: Demonstration
if __name__ == "__main__":
    manager = ToDoManager(JSONStorage())

    while True:
        print("\nTo-Do Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Filter Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (optional): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(Task(task_id, title, description, due_date, status))
            print("Task added successfully!")
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new title (or leave blank): ") or None
            description = input("Enter new description (or leave blank): ") or None
            due_date = input("Enter new due date (or leave blank): ") or None
            status = input("Enter new status (or leave blank): ") or None
            print(manager.update_task(task_id, title, description, due_date, status))
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)
            print("Task deleted successfully!")
        elif choice == "5":
            status = input("Enter status to filter by: ")
            tasks = manager.filter_tasks(status)
            for task in tasks:
                print(task)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            ##