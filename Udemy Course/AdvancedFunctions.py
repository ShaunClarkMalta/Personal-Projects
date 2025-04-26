hexnum = hex(1024)
print(f"Hexadecimal: {hexnum}")

binnum = bin(1024)
print(f"Binary Number: {binnum}")

print(pow(2,4))    #Same as 2**4
print(abs(-3))     #Absolute number
print(round(3.141529, 2))

set1 = {1,2,3,4}
print(set1)
set2 = set1.copy()
set2.add(5)
print(f"Difference: {set2.difference(set1)}")       #Shows elements that are different
print(f"Intersection: {set1.intersection(set2)}")   #Shows common elements