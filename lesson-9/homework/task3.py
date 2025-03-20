import json
import csv


def load_tasks(file_path):
    """Load tasks1.json from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
        return []


def save_tasks(file_path, tasks):
    """Save tasks1.json back to the JSON file."""
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    """Display all tasks1.json in a readable format."""
    print("\nTask List:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")


def calculate_statistics(tasks):
    """Calculate and display task statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks1.json: {total_tasks}")
    print(f"Completed tasks1.json: {completed_tasks}")
    print(f"Pending tasks1.json: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")


def convert_json_to_csv(json_file, csv_file):
    """Convert tasks1.json.json to tasks1.json.csv."""
    tasks = load_tasks(json_file)
    if not tasks:
        return

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

    print(f"\nTasks successfully converted to {csv_file}")


# File paths
tasks_file = 'tasks.json'
csv_file = 'tasks.csv'

# Load and process tasks1.json
tasks = load_tasks(tasks_file)
if tasks:
    display_tasks(tasks)
    calculate_statistics(tasks)
    convert_json_to_csv(tasks_file, csv_file)
else:
    print("No tasks1.json to process.")