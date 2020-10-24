import math

velocidade = float(input('que velocidade? '))

angulo = float(input('e que angulo? '))

def distancia(velocidade, angulo):
    d = ((velocidade**2)*math.sin(2*angulo))/9.8
    if d<=98:
        return('Muito perto')
    elif d>=102:
        return('Muito longe')
    else:
        return('Acertou!')
        
print(distancia(velocidade, angulo))