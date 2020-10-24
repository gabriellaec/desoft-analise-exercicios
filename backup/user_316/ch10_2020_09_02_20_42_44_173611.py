import math

def volume_da_pizza(z, a):
    ab = math.pi * (z**2)
    return ab * a

print(volume_da_pizza(10, 5))