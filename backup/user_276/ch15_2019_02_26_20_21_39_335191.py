import math 
def volume_da_pizza(r, a):
    volume = math.pi * r**2 * a
    return volume
h = volume_da_pizza(3, 2)
print(h)