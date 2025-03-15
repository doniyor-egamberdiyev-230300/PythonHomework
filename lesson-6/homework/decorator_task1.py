def check(func):

    def wrapper(a, b):
        if b == 0:
            return
        return func(a, b)

    return wrapper


@check
def div(a, b):
    return a / b



if __name__ == "__main__":
    print(div(6, 2))
    print(div(6, 0))




def add_employee(employee_id, name, position, salary):

    with open("employees.txt", "a") as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")


if __name__ == "__main__":

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    add_employee(emp_id, name, position, salary)
    print("Employee record added successfully.")
