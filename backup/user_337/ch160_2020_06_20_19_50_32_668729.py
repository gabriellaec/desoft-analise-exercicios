import math
dif = 0 
for g in range(0,91):
    f = math.sin(math.radians(g))
    b = (4*g*(180-g))/(40500 - g*(180-g))
    if abs(f - b) > dif:
        dif = abs(f - b)
        grau = g

print(grau)
