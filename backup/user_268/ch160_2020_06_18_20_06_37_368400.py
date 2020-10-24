import math
dif = []

for i in range(91):
    b = ((4*i) * (180 - i))/ (40500 - (i * (180 - i)))
    r = math.radians(i)
    s = math.sin(r)
    a = s - b
    x = abs(a)
    dif.append(x)


m = max(dif)

for i in range(dif):
    if dif[i] == m:
        print(i)
        break
    