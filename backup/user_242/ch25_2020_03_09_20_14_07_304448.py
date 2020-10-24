import math
v = float (input('qual a velocidade?'))
theta = float (input('qual o Ângulo?'))
def calcula_distancia_do_projetil(v,theta):
    d = ((v**2) * math.sin(math.radians (2*theta)))/9.8
    if d == 98:
        return 'Acertou'
    elif 90 <= d <98 and 99 <= d < 100:
        return 'Muito perto'
    else:
        return 'Muito longe'

print (calcula_distancia_do_projetil(v,theta))