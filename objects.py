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
