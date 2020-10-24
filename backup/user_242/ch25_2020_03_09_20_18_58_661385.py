import math
v = float (input('Qual a velocidade?'))
theta = float (input('Qual o Ângulo?'))
def calcula_distancia_do_projetil(v,theta):
    d = ((v**2) * math.sin(math.radians(2*theta)))/9.8
    if d > 102:
        return 'Muito longe'
    elif d < 98:
        return 'Muito perto'
    else:
        return 'Acertou!'

print (calcula_distancia_do_projetil(v,theta))