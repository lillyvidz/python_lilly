attend=200
var1=input("enter student name:")
cls=int(input("enter attended class:"))
print(var1)
print(cls)
p=(cls*100)/attend
print(p)
if p==100:
    print("eligible1")
elif p>=80:
    print("eligible2")
elif p>=75:
    print("eligible3")
else:
    print("not elogible")