import math
for x in range(91):
    sin = (4 * x * (180 - x)) / (40500 - x * (180 - x))
    a = math.sin(math.radians(x))
    diferencas = []
    d = a - sin
    diferencas.append(d)
    if d[x] > d[x - 1]:
        diferença = d[x]
        print (x)