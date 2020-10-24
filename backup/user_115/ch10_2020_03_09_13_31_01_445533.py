#V=πr^2h

from math import pi

def volume_da_pizza(z, a):
    v = pi * z**2 * a
    return v

z = 20
a = 5

print(volume_da_pizza(z, a))