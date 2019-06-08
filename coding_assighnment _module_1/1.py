inp = input("Enter comma separated integers: ")
list = inp.split (",")
li = []
for i in list:
	li.append(int(i))

print(li)
na=tuple(li)
print(na)
