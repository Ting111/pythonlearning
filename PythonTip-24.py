m, n = 6, 5
def f(m, n):
    a = min(m, n)
    b = max(m, n)
    if a == 1 and b != 2:
    	return -1
    elif (a + b) % 3 == 0:
    	return (a + b) // 3
    elif (a + b) % 3 == 1:
    	return (a + b) // 3 + 3
    else :
    	return (a + b) // 3 + 2
print(f(m, n))