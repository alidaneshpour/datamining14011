b = 0
y = 0
a = True
while a == True:
    n = int(input("enter number: "))
    if n > b:
        y = b
        b = n
    elif n > y:
        y = n
    if n == -1:
        a = False

print(b, y)
