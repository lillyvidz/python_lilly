from datetime import date
print("CUSTOMER INFORMATION")
print("_____________________")
print("Enter first name:")
var1=input()
print("Enter last name:")
var2=input()
print("Enter dob in yyyy:")
var3=int(input())
today = date.today()
print("Your Informtion are:")
print("_____________________")

print(var1)
print(var2)
print(var3)
print("Today date is: ", today)
age=today.year-var3
print("age:",age)
