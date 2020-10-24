import math
ls = []
for i in range(91):
    sinx = (4*i*(180-i))/(40500-i*(180-i))
    math = math.sin(i)
    ls.append(abs(sinx)-abs(math))
print(max(ls))