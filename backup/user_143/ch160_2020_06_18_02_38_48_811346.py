import math
x = []
b = 0
x.append(b)
for j in range (0, 90, 1):
    b += 1
    x.append(b)
dife = []
for i in x:
    senx = (4 * i * (180 - i)) / (40500 - i * (180 - i))
    k = math.sin(math.radians(i))
    print(k)
    print(senx)
    dif = abs(senx - k)
    dife.append(dif)
a = max(dife)
print (c)