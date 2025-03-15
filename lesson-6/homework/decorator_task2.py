def check(func):

    def wrapper(a, b):
        return "Denominator can't be zero" if b == 0 else func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

FILENAME = "employees.txt"

def modify_file(emp_id, new_data=None, delete=False):

    with open(FILENAME, "r") as file:
        records = file.readlines()
    with open(FILENAME, "w") as file:
        for record in records:
            if record.startswith(emp_id + ","):
                if delete:
                    continue
                file.write(new_data + "\n")
            else:
                file.write(record)

def add_employee():
    with open(FILENAME, "a") as file:
        file.write(input("Enter Employee ID, Name, Position, Salary: ") + "\n")

def view_employees():
    try:
        with open(FILENAME, "r") as file:
            print(file.read() or "No records found.")
    except FileNotFoundError:
        print("No records found.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open(FILENAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Found:", record.strip())
                return
    print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    new_data = input("Enter updated Name, Position, Salary: ")
    modify_file(emp_id, f"{emp_id}, {new_data}")

def delete_employee():
    modify_file(input("Enter Employee ID to delete: "), delete=True)

def main():
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
