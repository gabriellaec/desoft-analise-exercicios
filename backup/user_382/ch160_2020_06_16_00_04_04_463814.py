from math import * 

l1 = []

for 0 in range(1,90,1):
    sin_x = (4*i*(180 - i))/(40500 - i*(180-i))
    valor = sin(radians(i))
    l1.append(abs(sin_x - valor))    
    
print(max(l1))

