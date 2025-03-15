FILENAME = "employees.txt"

def modify_file(emp_id, new_data=None, delete=False):
    """Helper function to update or delete employee records."""
    with open(FILENAME, "r") as file:
        records = file.readlines()
    with open(FILENAME, "w") as file:
        found = False
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                if delete:
                    continue
                file.write(new_data + "\n")
            else:
                file.write(record)
        return found

def add_employee():
    """Append a new employee record."""
    with open(FILENAME, "a") as file:
        file.write(input("Enter Employee ID, Name, Position, Salary: ") + "\n")
    print("Employee record added.")

def view_employees():
    """Display all employee records."""
    try:
        with open(FILENAME, "r") as file:
            content = file.read().strip()
            print(content if content else "No records found.")
    except FileNotFoundError:
        print("No records found.")

def search_employee():
    """Search for an employee by Employee ID."""
    emp_id = input("Enter Employee ID to search: ")
    with open(FILENAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Found:", record.strip())
                return
    print("Employee not found.")

def update_employee():
    """Update an employee's information."""
    emp_id = input("Enter Employee ID to update: ")
    new_data = input("Enter updated Name, Position, Salary: ")
    if modify_file(emp_id, f"{emp_id}, {new_data}"):
        print("Employee updated.")
    else:
        print("Employee not found.")

def delete_employee():
    """Delete an employee record."""
    if modify_file(input("Enter Employee ID to delete: "), delete=True):
        print("Employee deleted.")
    else:
        print("Employee not found.")

def main():
    """Menu-driven interface for managing employee records."""
    options = {
        "1": add_employee,
        "2": view_employees,
        "3": search_employee,
        "4": update_employee,
        "5": delete_employee,
        "6": exit
    }
    while True:
        print("\n1. Add  2. View  3. Search  4. Update  5. Delete  6. Exit")
        options.get(input("Choose an option: "), lambda: print("Invalid choice"))()

if __name__ == "__main__":
    main()
