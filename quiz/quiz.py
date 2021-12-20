"""
s = a+ aa + aaa+ aaaa + aaaaa +...
求s
"""
a = 5
n = 6
'''
 5 + 55 + 555 + 5555 + 55555 + 555555
	555555= 5*10**5 + 5*10**4 + 5*10**3 + 5*10**2 + 5*10**1 + 5*10**0 
'''
# print(5*10**4)
s = 0
next_a = 0
for i in range(n):
	next_a += a * 10 ** i
	print(next_a)
	s += next_a
print(s)
