set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"apple", "banana", "cherry","carrot"}
print(set1)
set1.add("pine")
print(set1)
print("cherry" in set1)
s1=set1.union({"apple","orange"})
print(s1)
s2=set1.intersection({"apple","grapes"})
print(s2)

s3=set1.union(set4)
print(s3)

print(set1.isdisjoint(set2))