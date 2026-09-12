print("===== number =====")
# in JAVA ,variable is a name of storage location!
# in Python ,variable is named references!

count = 100
count_type = type(count)
print(f"the coumt :{count} and type :{count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)
