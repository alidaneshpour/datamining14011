m = 0
a = True
while a == True:
    n = int(input("enter number: "))
    if n > m:
        m = n
    if n == -1:
        a = False

print(m)
