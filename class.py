class Employee:
    empCount=0
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("total Employee%d"% Employee.empCount)
    
    def displayEmployee(self):
        print("Name:",self.name,'salary:',self.salary)

    "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2=Employee('bramuel', 12000)
"This would create third object of Employee class"
emp3=Employee('chris', 34000)
emp4= Employee("zenah", 756656)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print("total Employee%d"% Employee.empCount)


