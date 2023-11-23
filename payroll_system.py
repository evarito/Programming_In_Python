#the code implements OOP concepts calculating the payroll of a salaried employee, horly employee and an employee who gets a comission 

class employee: # a super class that contains the basic information of an employee
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name 



class S_employee(employee):# this class inherits from the employee class to get the names and employee id 
    def __init__(self, employee_id, name, Salary):
        super().__init__(employee_id, name)# calls the constructor of the superclass 
        self.Salary = Salary

    def CalcPayroll(self):
        return self.Salary
    

class H_employee(employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)# claas the constructor of the superclass 
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def CalcPayroll(self):
        return self.hourly_rate * self.hours_worked
    


class ComEmployee(S_employee):
    def __init__(self, employee_id, name, Salary, com_rate, sales):
        super().__init__(employee_id, name, Salary)#calls the constructor of the child class(S_employee, which has the constructor of the superclass )
        self.com_rate = com_rate
        self.sales = sales 


    def Calc_commision(self):
        return self.com_rate * self.sales 
    


salary_employee = S_employee(employee_id=789, name="Newton Doe", Salary=400000)
hourly_employee = H_employee(employee_id=900, name="Milcha Waweru", hourly_rate=30, hours_worked=60)
comission_employee = ComEmployee(employee_id=456, name="Yusuf Abdi", Salary=70000, com_rate=0.5, sales=700000)

print(f"Payroll for Salaried Empoyee: Ksh.{salary_employee.CalcPayroll()}")
print(f"Payroll for Hourly Employee: Ksh.{hourly_employee.CalcPayroll()}")
print(f"Payroll for Comission Employee: Ksh.{comission_employee.Calc_commision()}") 


    

    
