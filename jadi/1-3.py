a = int(input("enter number"))
b1 = a % 10
c1 = int(a/10)
b2 = c1 % 10
b3 = int(c1 / 10)
d = b3+10*b2+100*b1

print(2*d)
