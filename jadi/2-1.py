t = 50
f = 0
g = 0
javab = False
print(t)
p = input("enter char: ")
while javab == False:
    if p == "b":
        m = t
        t = int(t+abs((f-t))/2)
        print(t)
        p = input("enter char: ")
        f = m
    elif p == "k":
        m = t
        t = int((t-abs((t-f))/2))
        print(t)
        p = input("enter char: ")
        f = m
    else:
        print("d")
        javab = True
