import math
ls = []
for i in range(0,91,1):
    sinx = (4*i*(180-i))/(40500-i*(180-i))
    math = math.sin(math.radians(i))
    ls.append(abs(sinx)-abs(math))
print(max(ls))