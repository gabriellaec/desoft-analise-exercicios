from math import pi

def volume_da_pizza(r, h):
    v = pi*(r**2)*h
    return v

print (volume_da_pizza(10, 5))