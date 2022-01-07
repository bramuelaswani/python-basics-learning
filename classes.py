# class robot:
#     def introduce_self(self):
#         print("my name is" + " "+ self.name)
# r1=robot()
# r1.name="Tom"
# r1.color="red"
# r1.weight=30

# r2=robot()
# r2.name="Jerry"
# r2.color="Blue"
# r2.weight=40

# r1.introduce_self()
# r2.introduce_self()


# class robot:
#     def __init__(self,name,color,weight):
#         self.name=name
#         self.color=color
#         self.weight=weight
#     def introduce_self(self):
#                 print("my name is" + " "+ self.name)

# r1=robot("Tom", "red",30)
# r2=robot("jerry",'blue',40)

# r1.introduce_self()
# r2.introduce_self()


class employee:
    raise_amount=1.04
    num_of_emp=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + "." + last + "@company.com"
        employee.num_of_emp+=1

    def fullname(self):
        return "{},{}".format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

emp_1=employee("bramuel","aswan",50000)
emp_2=employee("brian","cheye",60000)

#employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)
#print("{},{}".format(emp_1.first,emp_1.last)) # but this long
print(emp_1.fullname())
print(emp_2.fullname())
print(employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#employee.raise_amount=1.05
emp_1.raise_amount=1.05

print(emp_1.__dict__)
print(employee.__dict__)

print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(employee.num_of_emp)


