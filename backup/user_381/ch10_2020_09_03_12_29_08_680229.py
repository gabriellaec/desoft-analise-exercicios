import math
def volume_da_pizza(z,a):
    volume = math.pi*a*(z)**2
    return volume

a=1
z=2
volume = volume_da_pizza(z,a)
print(volume)