from math import *
ls = []
for i in range(0,91,1):
    sinx = (4*i(180-i))/(40500-i(180-i))
    math = sin(i)
    ls.append(abs(sinx)-abs(math))
print(max(ls))