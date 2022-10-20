n = input("enter str: ")
c = -1
k = -1
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []

for i in n:
    c = c+1
    if i == 'h':
        a1.append(c)

c = -1
for i in n:
    c = c+1
    if i == 'e':
        a2.append(c)

c = -1
for i in n:
    c = c+1
    if i == 'l':
        a3.append(c)

c = -1
for i in n:
    c = c+1
    if i == 'l':
        a4.append(c)

c = -1
for i in n:
    c = c+1
    if i == 'o':
        a5.append(c)

print(a1, a2, a3, a4, a5)

hhhh = len(a1)*len(a2)*len(a3)*len(a4)*len(a5)

cc = 0
kkk = True
ttt = 0
xxx = False
while kkk == True:
    for i in a1:
        for j in a2:
            for z in a3:
                for k in a4:
                    for p in a5:
                        ttt = ttt+1
                        if p > k & k > z & z > j & j > i:
                            xxx = True
                            kkk = False
                        elif ttt > hhhh:
                            kkk = False

    kkk = False


if xxx == True:
    print('YES')
else:
    print('NO')
