n = input("enter str: ")
m = n.upper()
c = 0
t = -1
for i in n:
    t = t+1
    if i == m[t]:
        c = c+1

if c > len(n)-c:
    n = n.upper()
else:
    n = n.lower()


print(n)
