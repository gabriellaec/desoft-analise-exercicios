import math
def distancia(velocidade, teta):
    y = velocidade*velocidade*math.sin(math.radians(2*teta))/9.8 
    return y
velocidade = float(input('Qual a velocidade? '))
teta = float(input('Qual o angulo? '))
if distancia(velocidade, teta) < 98 :
    print('Muito perto')
elif distancia (velocidade, teta) > 102:
    print('Muito longe')
else:
    print('Acertou!')