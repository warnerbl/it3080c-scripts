

print("Please enter your birthday")
birthYear = input("Year: ")
birthMonth = input("Month (1-12): ")
birthDay = input("Day: ")

from datetime import datetime
now = datetime.now()

age = datetime(int(birthYear),int(birthMonth), int(birthDay))

ageCalcuated = now - age 
ageInSeconds = ageCalcuated.days * 86400
print("your age in seconds is: " + str(ageInSeconds))