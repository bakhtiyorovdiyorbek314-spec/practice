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
