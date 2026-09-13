'''
CLASS:
    (1) What is class
    (2)ordinary vs static class
    (3) special methods
'''


print("==== What is class  =====")
# class - blueprint for object creation
# structer-state constuctor method


class Person():
    # state
    message = "static state property"

    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method

    def introduce(self):
        print(f"{self.name} says:How do you do!")

    def say_age(self):
        print(f"{self.name} says:I am {self.age} years old")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Deen", 24)
person2 = Person("Steve", 24)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("==== ordinary vs static class=====")

# Static property lar Object bilan emas ,togridan rogri Class bn keladigan propertylar
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()


print("==== special/magic methods=====")
# Python's most common magic method are below:
# __init__, __new__,__str__,__call__, __getitem__, __eq__ ,__len__...


class Car():
    # state
    description = "our class makes car"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # ordinary method
    def start_engine(self):
        print(f"the {self.name} started engine")

    def stop_engine(self):
        print(f"the {self.name} stoped engine")

    # magic method

    def __str__(self):
        return f"{self.name} was produced in {self.year}"

    def __call__(self):
        print("Object called as functions")
        return True


my_car = Car("Lamborgini", 2020)

my_car.start_engine()
my_car.stop_engine()

print("-------")
your_car = Car("BENZ", 2023)
print(your_car)

response = your_car()
print("response:", response)
