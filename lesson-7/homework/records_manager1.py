import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w"): pass

    def add_employee(self, employee):
        if self.is_duplicate_id(employee.employee_id):
            print("Error: Employee ID must be unique.")
            return

        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self, sort_by=None):
        employees = self.load_employees()
        if not employees:
            print("No records found.")
            return

        if sort_by == "salary":
            employees.sort(key=lambda emp: emp.salary)
        elif sort_by == "name":
            employees.sort(key=lambda emp: emp.name)

        print("Employee Records:")
        for emp in employees:
            print(emp)

    def search_employee(self, employee_id):
        employees = self.load_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(emp)
                return emp
        print("Employee not found.")
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employees = self.load_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                if name:
                    emp.name = name
                if position:
                    emp.position = position
                if salary:
                    emp.salary = float(salary)
                self.save_employees(employees)
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self, employee_id):
        employees = self.load_employees()
        employees = [emp for emp in employees if emp.employee_id != employee_id]
        self.save_employees(employees)
        print("Employee deleted successfully!")

    def is_duplicate_id(self, employee_id):
        employees = self.load_employees()
        return any(emp.employee_id == employee_id for emp in employees)

    def load_employees(self):
        employees = []
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    if len(parts) == 4:
                        employees.append(Employee(parts[0], parts[1], parts[2], parts[3]))
        except FileNotFoundError:
            print("Error: File not found.")
        return employees

    def save_employees(self, employees):
        with open(self.FILE_NAME, "w") as file:
            for emp in employees:
                file.write(str(emp) + "\n")

    def menu(self):
        while True:
            print("""
Welcome to Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
            choice = input("Enter your choice: ")

            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(emp_id, name, position, salary))
            elif choice == "2":
                sort_by = input("Sort by (name/salary/none): ").strip().lower()
                self.view_all_employees(sort_by if sort_by in ["name", "salary"] else None)
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                self.search_employee(emp_id)
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (or press Enter to skip): ") or None
                position = input("Enter new Position (or press Enter to skip): ") or None
                salary = input("Enter new Salary (or press Enter to skip): ") or None
                self.update_employee(emp_id, name, position, salary)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_employee(emp_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()