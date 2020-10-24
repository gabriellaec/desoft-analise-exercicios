import math

def alcance(v, alpha):
    distancia = ((v**2)*math.sin(2*alpha*math.pi/180))/9.8
    return distancia

velocidade = 31.4
angulo = 45

distancia_do_tiro = alcance(velocidade, angulo)

if distancia_do_tiro < 98:
    print('Muito perto')
elif distancia_do_tiro >= 98 and distancia_do_tiro <= 102:
    print('Acertou!')
else:
    print('Muito longe')

print('A distância do seu tiro foi de {0} metros'.format(distancia_do_tiro))