import math
def distancia(v,θ):
    distancia = ((v**2)*(math.sin(2*θ)))/(9.8)
    return distancia
if distancia < 100:
    print('Muito perto!')
elif distancia == 100:
    print('Acertou!')
else:
    print('Muito longe!')