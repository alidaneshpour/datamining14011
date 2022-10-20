import math
f = False
n = int(input("enter number: "))
m = math.ceil(math.sqrt(n))
for i in range(2, m):
    if n % i == 0:
        print("not prime")
        f = True
        break
if f == False:
    print("prime")
