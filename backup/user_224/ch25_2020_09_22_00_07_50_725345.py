import math
θ = int(input('Digite o angulo da catapulta em graus  '))
v = int(input('Digite a velocidade do alvo em metros/segundo  '))
g = 9.8
def distancia_atingida(θ,v):
    d = int(v**2*math.sin(math.radians(2*θ))/g)
    return d

resultado = distancia_atingida(θ,v)

if resultado < 98 :
    print('Muito perto')
elif resultado > 102 :
    print('Muito longe')
else:
    print('Acertou!')

print(resultado)


