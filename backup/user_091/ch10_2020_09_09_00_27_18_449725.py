import math
def volume_da_pizza(z,a):
    volume = (math.pi*(z**2))*a
    return volume
r=1
h=2
z= volume_da_pizza(r,h)
print(z)