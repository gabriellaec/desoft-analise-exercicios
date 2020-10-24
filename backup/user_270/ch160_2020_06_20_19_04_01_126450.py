import math

def sin(x):
    sinx = (4*x*(180-x))/(40500-x*(180-x))
    return sinx
list = []
i = 0
v = 0
for x in range(0,91):
    sin1 = math.sin(math.radians(x))
    list.append(sin1-sin(x))
    if abs(list[x]) > v:
        i = x
        v = abs(list[x])
print(i)