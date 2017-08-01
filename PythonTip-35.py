L=[-2,-3,3,50,1,60,7,-4,8,6,36,2,4,-5,-7,141,12]
a, b = [], 0

for i in L:
	if i >= 0:
		b += i
	else:
		b = 0
	a.append(b)

print(max(a))