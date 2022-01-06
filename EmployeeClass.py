class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary,age):
      self.name = name
      self.salary = salary
      self.age=age
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary, "age:",self.age)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000,32)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000,45)
emp3=Employee('cheye', 3566464,34)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print ("Total Employee %d" % Employee.empCount)