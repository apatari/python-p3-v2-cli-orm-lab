from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the name: ")
    employee = Employee.find_by_name(name)
    if employee: print(employee) 
    else: print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter id: ")
    employee = Employee.find_by_id(id_)
    if employee: print(employee)
    else: print(f'No Employee matching id# {id_}')


def create_employee():
    name = input('Enter employee name: ')
    title = input("Enter employee job title: ")
    department_id_ = int(input('Enter department id#: '))
    try:
        employee = Employee.create(name, title, department_id_)
        print(f'Employee created: {employee}')
    except Exception as exc:
        print('Error creating employee: ', exc)


def update_employee():
    id_ = input("Enter employee id to update: ")
    employee = Employee.find_by_id(id_)
    if employee:
        try:
            name = input("Enter new employee name: ")
            employee.name = name
            title = input("Enter new job title: ")
            employee.job_title = title
            department_id_ = int(input("Enter new department_id: "))
            employee.department_id = department_id_
                        
            employee.update()
            print(f'Employee updated: {employee}')
        except Exception as exc:
            print(f'Error updating employee: ', exc)
    else:
        print(f'Employee with id# {id_} not found')


def delete_employee():
    id_ = input('Enter employee id#: ')
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print('\n' , f'Invalid employee id: {id_}', end='\n\n')


def list_department_employees():
    dept_id_ = int(input('Enter the department id: '))
    department = Department.find_by_id(dept_id_)
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)


    else:
        print(f'{dept_id_} is an invalid department id')
    
    