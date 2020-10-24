import math
def volume_da_pizza(z, a):
    volume=(z**2)*a*math.pi
    return volume
z=int(input('raio da pizza'))
a=int(input('altura da pizza'))
print(volume_da_pizza(z,a))