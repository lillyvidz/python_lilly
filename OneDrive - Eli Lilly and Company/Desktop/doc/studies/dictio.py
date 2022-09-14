tp=(1,2,3)
print(tp) #it can't be changed immutable so no operation

#dict in the form of key value pairs
#set multiple set function,UNION,INTERSECT
d1={"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(d1)
print(len(d1))
d2={"brand": "Ford",
  "model": "Mustang",
  "year": 1964,"buy":{"you": "me","i": "u"}}
print(d2)

d2["buy"]="php"
print(d2)

d2["test2"]="mine"
del d2["year"]
print(d2)

d2.update({"brand":"bmw"})
print(d2)
print("_______________________________________________________")
d3={"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(d3)
print(d3.values())
result=input("enter key value:")
print(d3[result])
"""res=input("ente vakues:")
print(d3(res)) """


