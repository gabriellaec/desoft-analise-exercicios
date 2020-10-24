import math
def volume_da_pizza(z, a):
    vp = math.pi * z**2 * a
    return vp
m = 10;
n = 10;
p = volume_da_pizza(m, n);
print(p);