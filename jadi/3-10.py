a = []
b = []
c = 0
n = int(input("enter number of laptops: "))
for i in range(0, n):
    p = int(input("enter price: "))
    q = int(input("enter quality: "))
    a.append(p)
    b.append(q)

for i in range(0, len(a)):
    for j in range(0, len(a)):
        if a[i] < a[j] & b[i] > b[j]:
            c = c+1
            break
    if a[i] < a[j] & b[i] > b[j]:
        break


if c >= 1:
    print('happy irsa', c)
else:
    print('poor irsa', c)
