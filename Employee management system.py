class Employee:
    def __init__(self, emp_id, name, department, salary, email, phone, experience):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.email = email
        self.phone = phone
        self.experience = experience
        self.attendance = 0
        self.leave_balance = 20

    def display(self):
        print("\n=======================")
        print("EMPLOYEE DETAILS")
        print("=======================")
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Experience:", self.experience)
        print("Attendance:", self.attendance)
        print("Leave Balance:", self.leave_balance)

    def mark_attendance(self):
        self.attendance += 1
        print("Attendance Updated Successfully")

    def increment_salary(self, percent):
        increment_amount = self.salary * percent / 100
        self.salary += increment_amount
        print("Salary Updated Successfully")

    def calculate_bonus(self):
        if self.attendance >= 25:
            return 5000
        elif self.attendance >= 15:
            return 3000
        else:
            return 1000

    def apply_leave(self, days):
        if days <= self.leave_balance:
            self.leave_balance -= days
            print("Leave Approved")
        else:
            print("Insufficient Leave Balance")

    def show_leave_balance(self):
        print("Remaining Leave Balance:", self.leave_balance)

    def transfer_department(self, new_department):
        old_department = self.department
        self.department = new_department
        print(f"Transferred from {old_department} to {new_department}")

    def generate_salary_slip(self):
        bonus = self.calculate_bonus()
        net_salary = self.salary + bonus

        print("\n=========================")
        print("SALARY SLIP")
        print("=========================")
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Basic Salary:", self.salary)
        print("Bonus:", bonus)
        print("=========================")
        print("Net Salary:", net_salary)
        print("=========================")

    def get_salary(self):
        return self.salary


employees = []


def add_employee():
    print("\nADD EMPLOYEE")

    emp_id = int(input("Enter Employee Id: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    experience = int(input("Enter Experience: "))

    emp = Employee(
        emp_id,
        name,
        department,
        salary,
        email,
        phone,
        experience
    )

    employees.append(emp)

    print("Employee Added Successfully")


def view_employees():
    if len(employees) == 0:
        print("No Employees Found")
        return

    for emp in employees:
        emp.display()


def search_employee():
    emp_id = int(input("Enter Employee Id: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            emp.display()
            return emp

    print("Employee Not Found")
    return None


def remove_employee():
    emp_id = int(input("Enter Employee Id: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee Removed Successfully")
            return

    print("Employee Not Found")


def mark_attendance():
    emp = search_employee()

    if emp:
        emp.mark_attendance()


def update_salary():
    emp = search_employee()

    if emp:
        percentage = float(input("Enter Increment Percentage: "))
        emp.increment_salary(percentage)


def calculate_bonus():
    emp = search_employee()

    if emp:
        print("Bonus Amount:", emp.calculate_bonus())


def apply_leave():
    emp = search_employee()

    if emp:
        days = int(input("Enter Number of Leave Days: "))
        emp.apply_leave(days)


def show_leave_balance():
    emp = search_employee()

    if emp:
        emp.show_leave_balance()


def transfer_department():
    emp = search_employee()

    if emp:
        new_department = input("Enter New Department: ")
        emp.transfer_department(new_department)


def generate_salary_slip():
    emp = search_employee()

    if emp:
        emp.generate_salary_slip()


def get_salary():
    emp = search_employee()

    if emp:
        print("Current Salary:", emp.get_salary())


while True:

    print("\n================================")
    print("SMART HR MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Mark Attendance")
    print("6. Update Salary")
    print("7. Calculate Bonus")
    print("8. Apply Leave")
    print("9. Show Leave Balance")
    print("10. Transfer Department")
    print("11. Generate Salary Slip")
    print("12. Get Salary")
    print("13. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        remove_employee()

    elif choice == 5:
        mark_attendance()

    elif choice == 6:
        update_salary()

    elif choice == 7:
        calculate_bonus()

    elif choice == 8:
        apply_leave()

    elif choice == 9:
        show_leave_balance()

    elif choice == 10:
        transfer_department()

    elif choice == 11:
        generate_salary_slip()

    elif choice == 12:
        get_salary()

    elif choice == 13:
        print("Thank You")
        break

    else:
        print("Invalid Choice")