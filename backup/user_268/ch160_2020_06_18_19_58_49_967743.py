import math
dif = []

for i in range(91):
    b = (4*i * (180 - i))/ (40500 - i * (180 - i))
    r = math.radians(i)
    s = math.sin(r)
    a = b - s
    ab = abs(a)
    dif.append(ab)

absoluto = abs(dif)
print(absoluto)
    