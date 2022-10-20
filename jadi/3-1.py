n = input("enter str: ")
n = n.lower()
z1 = n.replace('a', '')
z2 = z1.replace('i', '')
z3 = z2.replace('o', '')
z4 = z3.replace('u', '')
z5 = z4.replace('e', '')
print(z5)

t = len(z5)
m = ''
for i in range(0, t):
    m = m + '.' + z5[i]

m = m.lower()
print(m)
