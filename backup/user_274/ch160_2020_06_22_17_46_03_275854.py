import math
a = 0

for i in range(91):
    c = math.radians(i)
    x = math.sin(c)
    x = math.degrees(x)
    y = (4*i*(180-x))/(40500 - x*(180-x))
    e = abs(x-y)
    if e > a:
        a = e
        
print(a)