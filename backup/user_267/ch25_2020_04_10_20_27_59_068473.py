import math
g = 9.8
def distancia(v, theta):
    d = ((v**2)*math.sin((math.radians(angulo))*2))/g
    if d < 98:
        return 'Muito perto'
    elif d > 102:
        return 'Muito longe'
    else: 
        return 'Acertou!'

v = float(input('Qual a velocidade? '))
theta = float(input('Qual o ângulo? '))
print(distancia(v, theta))
    