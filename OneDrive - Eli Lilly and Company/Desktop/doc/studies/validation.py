"""import phonenumbers
  
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber = phonenumbers.parse("+919876543210")
  
# This will print the phone number and 
# it's basic details.
print(phoneNumber)"""
ent=(input("how many enteries:"))
while len(ent)>0:
    print("enter properly")
    ent = ent+1
    

    name=str(input("enter your name:"))
    for names in {name}:
        if int(len(name))>2 and name.isalpha():
            print(name)
        else:
            print("invalid")
            
    age=int(input("Enter age:"))
    if age<18:
        print("invalid")
    else:
        print(age)
        
    pnum=(input("enter pnum:"))
    if len(pnum) == 10:
        print(pnum)
    else:
        print("invalid")
    