print("===== Iterable objects & Range ======")
# Iterable objects > string, dict , tuple, list, range, map , filter

text = "MIT"
for letter in text:
    print(f"the letter: {letter}")   # har bittta harfini alohida olib beradi


range_obj = range(5)
print("range_obj:", range_obj)
for ele in range_obj:
    print(f"the element: {ele}")  # 0 dan 4 gacha bolgan array yasab beradi

print("===== DICTIONARY ======")

# Dictionary is JSON Object
person = {"name": "DEEN", "age": 24, "single": True}  # oddiy JSON
person_obj = dict(name="DEEN", age=24, single=True)  # Object JSON

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name1 = person_obj["name"]
print("name1:", name1)

# mavjud bolmagan state ni cgaqirib korsak Pythonda Xatolik beradi
# name2 = person_obj["hobby"]
# print("name2:", name2)


# bunday xatolikdan qochish uchun get() methodini qollaymiz
# method:get()
age = person_obj.get("age")
hobby = person_obj.get("hobby")  # None korinishida chiadi
balance = person_obj.get("balance", 0)  # default 0 qabul qiladi
print(f"the age :{age}, hobby:{hobby}, and balance: {balance}")

for key in person_obj:
    print(f"the key: {key}")

del person_obj["single"]  # state larni ochirib beradi
for key in person_obj:
    # key va value larni bir vaqtni ozida iterate qilib beradi
    print(f"the key: {key} => value:{person_obj.get(key)}")
