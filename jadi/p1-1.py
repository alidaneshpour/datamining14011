
def ma(n):
    b = []
    bb = [1]
    m = int((n+2)/2)
    if n > 1:
        for i in range(2, m):
            if n % i == 0:
                b.append(i)
        b.append(n)
        return(b)
    else:
        return(bb)


def tma(n):
    c = 0
    m = int((n+2)/2)
    if n > 1:
        for i in range(2, m):
            if n % i == 0:
                c += 1
        return(c+2)
    else:
        return(1)


a = []
c = []
d = []
e = []
p = []
k = []
u = []
x = []
javabjavab = []
counter = 0
for i in range(1, 11):
    n = int(input("enter number: "))
    a.append(n)
for i in range(1, 11):
    b = a.pop()
    c = ma(b)
    for z in range(0, len(c)):
        d = c.pop()
        e.append(tma(d))
    for j in range(0, len(e)):
        f = e.pop()
        if f == 2:
            counter += 1
    k.append(b)
    p.append(counter)
    # print(f"tedad maghsoomaliehaye avval {b}={counter}")
    counter = 0
javab = 0
gg = 0
u = p
for i in p:
    if i > gg:
        gg = i

uuu = p.index(gg)
jjj = p[uuu]
ccc = -1
for i in p:
    ccc = ccc+1
    if i == jjj:
        x.append(ccc)

for i in range(0, len(x)):
    hhhh = x.pop()
    ddd = k[hhhh]
    javabjavab.append(ddd)

javabjavab.sort()
mmm = javabjavab[-1]

print(mmm, jjj)
