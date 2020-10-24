import math
def calcula_volume_da_esfera(raio):
    volume = 4/3*math.pi*raio**3
    print("O volume da esfera é: {0}".format(volume))
r = float(input("Entre com o raio da esfera: "))
calcula_volume_da_esfera(r)
