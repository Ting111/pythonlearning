a, b, c = 2.2, 1.4, 2.0

if a + b > c and abs(a - b) < c:
	d = sorted([a, b, c])
	e = d[0] ** 2 + d[1] ** 2 - d[2] ** 2
	if e > 0:
		print('R')
	elif e == 0:
		print('Z')
	else:
		print('D')
else:
	print('W')