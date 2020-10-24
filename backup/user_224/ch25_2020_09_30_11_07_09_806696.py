import math
v = int(input('Digite a velocidade do alvo em metros/segundo  '))
θ = int(input('Digite o angulo da catapulta em graus  '))
g = 9.8
def distancia_atingida(v,θ):
    d = int((v**2*math.sin(math.radians(2*θ)))/g)
    return d

resultado = distancia_atingida(v,θ)

if resultado < 98 :
    print('Muito perto')
elif resultado > 100 :
    print('Muito longe')
elif resultado >= 98 and <= 100 :
    print('Acertou!')







