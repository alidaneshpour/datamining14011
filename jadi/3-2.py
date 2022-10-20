n = input("enter str: ")
m1 = n.count('1')
m2 = n.count('2')
m3 = n.count('3')
m4 = m1*'+1' + m2*'+2' + m3*'+3'
m5 = m4[1:]
print(m5)
