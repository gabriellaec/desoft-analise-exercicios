import math

def sin(x):
    sinx = (4*x*(180-x))/(40500-x*(180-x))
    return sinx
list = []
for x in range(0,91):
    sin1 = math.sin(math.radians(x))
    list.append(abs(sin1-sin(x)))
print(max(list))