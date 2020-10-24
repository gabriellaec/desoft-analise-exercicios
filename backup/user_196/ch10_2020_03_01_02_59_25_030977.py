from math import pi
def volume_da_pizza (raio, altura):
    volume_pizza = pi*(raio**2)*altura
    return volume_pizza
a=5
b=7
volume_cilindro = volume_da_pizza (a,b)
print (volume_cilindro)