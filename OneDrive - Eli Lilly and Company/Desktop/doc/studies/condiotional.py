# if ifelse elif in not and or
""" age=int(input("enter age greater than 18:"))
if(age<18):
    print("not")
else:    
 print("yes") """
 
"""c=20
if c>25:
     if c%2==0:
         print("v1")
     else:
        print("v2")
else:
      print("out")"""
      
"""result=int(input("enter marks:"))
if result==100:
    print("topper")
elif result>=80:
    print("disyinction")
elif result>=70:
    print("good")
else:
    print("cope up buddy")"""
lst = []   
res=int(input("how many numbers:"))
for n in range(res):
    numbers=int(input("enter nos:"))
    lst.append(numbers)
print("max is",max(lst))