class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Iam {self.name} and Iam {self.age} years old")

    def speak(self):
        print("I dont know")


class Cat(Pet):
    def speak(self):
        print("meow")


class Dog(Pet):
    def speak(self):
        print("bark")


class Fish(Pet):
    pass


p = Pet("tim", 19)
p.show()
p.speak()

c = Cat("bill", 29)
c.show()
c.speak()
d = Dog("jack", 20)
d.show()
d.speak()
f = Fish("bubbles", 10)
f.show()
f.speak()
