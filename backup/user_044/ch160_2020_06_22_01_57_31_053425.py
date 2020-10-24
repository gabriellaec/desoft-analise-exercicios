import math
ls = []
for i in range(0,91,1):
    sinx = (4*i*(180-i))/(40500-i*(180-i))
    math = math.sin(int(i))
    ls.append(abs(sinx)-abs(math))
print(math.degrees(max(ls)))