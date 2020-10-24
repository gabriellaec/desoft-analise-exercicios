import math

def volume_da_pizza(z, a):
    z += math.pi * (z ** 2)
    return z * a