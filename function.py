'''
FUNCTIONS:
(1) DEFINE vs CALL
(2) Parametr va argument
(3) Keyword & default argument
(4) Scope
'''
print("==== Define vs Call =====")
# build in functions: type() print() input()
# Function: reusable block of code
# Instead of {} in JAVA , Python uses indentations!

# DEFINE -build (parametr)


def greet(a):
    print(f"how do you do {a}")


def greeting(b):
    print('greeting is executed')
    return f"hello {b}"


# CALL -execute (argument)
result1 = greet('Deen')
print("result1:", result1)   # void function bolgani uchun none qaytardi

result2 = greeting('Steve')
print('result2', result2)


print("==== Keyword vs Default argument =====")
# Define


def give_greet(name, age=25):
    print("give_greet is executed ")
    return f"My name is {name} and i am {age} years old"


# CALL
result3 = give_greet("Deen", 24)
print('result3:', result3)   # bu oddiy agrument berish usuli

result4 = give_greet(name="Steve", age=24)
# bu KEYWORD argument berish usuli, call qismida yozing , oqilishi oson bolishi uchun kk
print('result4:', result4)


# bu holda age kiritilmagani uchun tepadan DEFAULT qilib oldi
result5 = give_greet("John")
print('result5:', result5)


print("==== SCOPE =====")

b = 200  # third

# Define


def calculate(a):
    c = a*40  # first
    print(f" c natija teng:{c}")


# CALL
calculate(5)


def calculate(a, b):
    c = a*b
    print(f" c natija teng:{c}")


# CALL
calculate(5, 50)  # second


def calculate(a):
    c = a*b
    print(f" c natija teng:{c}")


# CALL
calculate(5)

# SCOPE  Priority tushunchasi bilan keladi, bu berilgan argument larni qaysi birini olishni tanlashdir,
# (1) Function ichidan izlaydi> otherwise > (2) CALL qismdan izlaydi > (3) Tashqaridan oladi
