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
