import math
dif = []

for i in range(0, 91):
    b = (4*i (180 - i))/ (40500 - i * (180 - i))
    r = radian(i)
    s = math.sin(r)
    dif.append(b - r)
print(abs(dif))
    
    