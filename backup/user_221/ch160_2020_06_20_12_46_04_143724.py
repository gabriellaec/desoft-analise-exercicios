import math
i = 0
d = 0
while 0 <= i <= 90:
    y = math.sin(math.radians(i))
    z = (4*i*(180 - i))/(40500 - i*(180 - i))
    if abs(y - z) > d:
        d = abs(y - z)
    i += 1

print (d)