emp=input("enter emp name:")
yr=int(input("enter year of completion:"))
sal=int(input("enter sal:"))
print(emp)
print(yr)
if yr>=10:
    bonus=((15*sal)/100)
    final=sal+bonus
    print(final)
elif yr>=5 and yr<10:
      bonus=((10*sal)/100)
      final=sal+bonus
      print(final)
else:
    print("not")

    