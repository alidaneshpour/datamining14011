c = 0
m = 0
for i in range(1, 4):
    n = int(input("enter number: "))
    if n/3 == 1:
        c += 1
    else:
        m = m+n

g = m+c*3
print(g, c)
