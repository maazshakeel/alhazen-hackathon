name: str = ""
age: int = 0 
place: str = ""
phone_num: str = ""

name = str(input("Your Name: "))
if name == "":
    print("Please enter your Name!")
    exit(1)
try:
    age = int(input("Your Age: "))
except ValueError:
    print("Please enter your age!")
    exit(1)
place = str(input("Your Place: "))
if place == "":
    print("Please enter your Place!")
    exit(1)
try:
    phone_num = str(input("Your Phone Number: +62 "))
    if (len(phone_num) != 10):
        print("Please enter valid phone number!")
        exit(1)
except ValueError:
    print("Please enter your Phone Number!")
    exit(1)

print("Thank u for register to this page")
