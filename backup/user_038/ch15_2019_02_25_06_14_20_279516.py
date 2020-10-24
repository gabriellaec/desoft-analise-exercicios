import math
def volume_da_pizza(raio, altura):
    volume = math.pi*raio**2*altura
    print("O volume da pizza é {0}".format(volume))
z = float(input("Informe o raio da pizza: "))
a = float(input("Informe a altura da pizza: "))
volume_da_pizza(z, a)