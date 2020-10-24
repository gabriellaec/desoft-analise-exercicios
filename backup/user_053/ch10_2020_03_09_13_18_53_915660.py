from math import pi

def volume_da_pizza(z,a):
    volume=pi*z*z*a
    return volume

raio=5
altura=10
vol=volume_da_pizza(raio,altura)

print(vol)