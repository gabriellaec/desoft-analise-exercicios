import math
ls = []
for i in range(91):
    sinx = (4*i*(180-i))/(40500-i*(180-i))
    mat = math.sin(math.radians(i))
    ls.append(abs(sinx-mat))
print(max(ls))