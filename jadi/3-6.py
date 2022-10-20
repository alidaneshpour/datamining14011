n = input("enter str: ")
n = n.lower()
t = 0
c = 0
for i in n:
    t = t+1
    if i == n[len(n)-t]:
        c = c+1

if c == len(n):
    print('palindrome')
else:
    print('not palindrome')


# n = input("enter str: ")
# if len(n) % 2 == 0:
#     m = int((len(n)+1)/2)
#     h = n[m:]
#     g = n[:m]
# else:
#     m = int((len(n)+1)/2)
#     h = n[(m-1):]
#     g = n[:m]


# print(h, g)

# if h == g:
#     print('palindrome')
# else:
#     print('not palindrome')
