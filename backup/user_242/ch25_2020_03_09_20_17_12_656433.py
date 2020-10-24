import math
v = float (input('Qual a velocidade?'))
theta = float (input('Qual o Ângulo?'))
def calcula_distancia_do_projetil(v,theta):
    d = ((v**2) * math.sin(math.radians(2*theta)))/9.8
    if 98 <= d and d <= 102:
        return 'Acertou'
    elif d < 98:
        return 'Muito perto'
    else:
        return 'Muito longe'

print (calcula_distancia_do_projetil(v,theta))