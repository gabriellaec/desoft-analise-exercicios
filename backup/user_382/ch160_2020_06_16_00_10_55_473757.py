from math import * 

l1 = []
l2 = []

for i in range(0,91,1):
    sin_x = (4*i*(180 - i))/(40500 - i*(180-i))
    valor = sin(radians(i))
    l1.append(i)
    l2.append(abs(sin_x - valor))   

print(l1[l2.index(max(l2))]

