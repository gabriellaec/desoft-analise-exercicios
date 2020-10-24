import math

def distancia(v, theta):
	d = ((v**2)*math.sin(math.radians(angulo)*2)/9.8
    if d < 98:
        print('Muito perto')
    elif d > 102:
        print('Muito longe')
    else: 
        print('Acertou!')

velocidade = float(input('Qual a velocidade? '))
theta = float(input('Qual o ângulo? '))
print(distancia(velocidade, theta))
    