'''
OBJECTS:
(1) What is object
(2) Iterable objects & Range
(3) DICTIONARY
(4) Error handling system
'''

import array   # package/module  # external package lar kabi chawirib olish zarur
import math    # package ni hamma methodlari bilan birga chaqiramiz
from math import ceil, asin  # aynan qaysi methodi keerak bolsa shunday chaqiramiz
print("===== What is object ======")
# An object has state and method properties
# Everything is object in Python!

print(type('Hello world'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Bularning hammasi classdan yasalgan instanse yani OBJECT

result1 = math.ceil(66.4)  # CALL - math object ning ceil methodi
result2 = ceil(33.2)
print("result1:", result1)
print("result2:", result2)

print("===== Error handling system ======")
car_dict = dict(name="BMW", year=2026, electric=True)

# (1)XATOLIK BOLGANDA:

try:
    print("passed here")
    # bu yerda mavjud bolmagani uchun except ishga tushyapti
    result1 = car_dict["origin"]
    print("result1:", result1)
except KeyError as err:
    print("NO origin state property found:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")


# (2)XATOLIK BOLMAGANDA:

try:
    print("passed here")
    # mavjud bolgani uchun  else ishga tushyapti
    result1 = car_dict["year"]
    print("result1:", result1)
except KeyError as err:
    print("NO origin state property found:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")


# (3) BIR NECHTA XATOLIK TEKSHIRILGANDA:

try:
    print("passed here")
    # mavjud bolgani uchun  else ishga tushyapti
    result1 = car_dict["year"]
    a = car_dict.speed
    print("result1:", result1)
except (KeyError, AttributeError) as err:  # except qismiga shunday yoz
    print("ERROR:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")


# (4) HAR QANDAY XATOLIKKA TEKSHIRILGANDA:


try:
    print("passed here")
    # mavjud bolgani uchun  else ishga tushyapti
    result1 = car_dict["year"]
    a = car_dict.speed
    print("result1:", result1)
except Exception as err:  # except qismiga shunday yoz
    print(" general ERROR:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")
