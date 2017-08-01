a, n = 'abcedfd', 3
def f(a, n):

    for i in range(len(a)):
    	if a[i: i + n] in a[:: -1] and i + n <= len(a):
    		return 'YES'
    return 'NO'
print(f(a, n))