
n = int(input("enter players numbers: "))
numbers = int(input("enter years: ").split())
if len(numbers) != n:
    print(f"You have to enter {n} numbers exactly")
    quit()
print(numbers)
