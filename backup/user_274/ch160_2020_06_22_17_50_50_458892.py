import math
a = 0
b = 0

for i in range(91):
    c = math.radians(i)
    x = math.sin(c)
    y = (4*i*(180-i))/(40500 - i*(180-i))
    e = abs(x-y)
    if e > a:
        a = e
        b = i
        
print(b)