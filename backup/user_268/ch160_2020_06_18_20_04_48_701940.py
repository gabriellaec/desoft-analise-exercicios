import math
dif = []

for i in range(91):
    b = ((4*i) * (180 - i))/ (4050 - (i * (180 - i)))
    r = math.radians(i)
    s = math.sin(r)
    a = s - b
    x = abs(a)
    dif.append(x)


print(max(dif))
    