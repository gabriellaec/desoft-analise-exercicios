import math
def distancia_lancamento(velocidade,angulo):
    distancia=velocidade**2*math.sin(2*math.radians(angulo))/9.8
    return distancia
velocidade=float(input('Qual a velocidade do lançamento em m/s?'))
angulo=float(input('Qual o angulo em radianos do lançamento?'))
distancia=distancia_lancamento(velocidade,angulo)
if distancia>98 and distancia<102:
    print('Acertou')
elif distancia<=98:
    print('Muito perto')
else:
    print('Muito longe')
print (distancia)