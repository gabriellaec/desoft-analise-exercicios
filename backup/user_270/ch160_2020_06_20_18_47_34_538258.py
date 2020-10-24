import math

def sin(x):
    sinx = (4*x*(180-x))/(400500-x*(180-x))
    return sinx
list = []
for x in range(0,91):
    sin = math.sin(math.radians(x))
    list.append(abs(sin-sin(x)))