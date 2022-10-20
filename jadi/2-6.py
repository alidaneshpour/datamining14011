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


z = 0
b = 0
for i in range(1, 7):
    n = int(input("enter number: "))
    p = int(tma(n) or 0)
    if p >= z:
        z = tma(n)
        if b < n:
            b = n

print(b, z)
