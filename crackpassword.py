import random

ATM_PASSWORD = input("กรอกรหัสผ่าน = ")
result = ""
while result!=ATM_PASSWORD:
    result = ""
    for letter in range(len(ATM_PASSWORD)):
        list_number = random.choice("0123456789")
        result = "".join(list_number)+result
        print("Search = ",result)
print("CRACK PASSWORD IS ",result)