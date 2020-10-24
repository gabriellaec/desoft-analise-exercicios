import math
angulo = float(input('Digite o angulo da catapulta em graus  '))
velocidade = int(input('Digite a velocidade do alvo em metros/segundo  '))
g = 9.8
def distancia_atingida(alpha,v):
    d = v**2*math.sin(math.radians(2*alpha))/g
    return d

resultado = distancia_atingida(angulo,velocidade)

if resultado < 100 :
    print('Muito perto')
elif resultado > 100 :
    print('Muito longe')
else:
    print('Acertou!')


