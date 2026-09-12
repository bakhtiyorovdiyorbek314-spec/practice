print("===== number =====")
# in JAVA ,variable is a name of storage location!
# in Python ,variable is named references!

count = 100
count_type = type(count)
print(f"the coumt :{count} and type :{count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("===== string =====")
# Method: upper() lower() title() find() replace()

course = "AI Python Fullstack"

result = type(course)
print(f"the result(1):{result}")

result = course.upper()
print(f"the result(2):{result}")

result = course.title()
print(f"the result(3):{result}")

result = course.replace("Fullstack", "MasterClass")
print(f"the result(4):{result}")


print("===== boolean =====")
# functions > type() input( ) bool() int() str()

y = input("give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric:{result}")


# TRUTHY VS FALSY
# TRUTHY> True 10 -10 "mit"
# FALSY> FAlse 0 "" none

test_falsy = "" or False or 0 or None
print("test_falsy:", bool(test_falsy))

test_truthy = "ali" or -44 or True
print("test_truthy:", bool(test_truthy))
