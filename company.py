from employee import Employee
class Company:
    def __init__(self):
        self.employees=[]
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employee(self):
        print("Current employees:")
        for e in self.employees:
            print(e.fname,e.lname)
        print('-------------------')
    def pay_employees(self):
        print("Paying employees:")
        for e in self.employees:
            print("Paycheck for", e.fname,e.lname)
            print(f"Amount:${e.calculate_salary():,.2f}")



def main():
    my_company=Company()
    employee1= Employee('John','Doe',50000)
    my_company.add_employee(employee1)
    employee2= Employee('Lee','Doe',250000)
    my_company.add_employee(employee2)
    employee1= Employee('Bob','Brown',50000)
    my_company.add_employee(employee1)
    # print(my_company.employees)
    my_company.display_employee()
    my_company.pay_employees()
main()