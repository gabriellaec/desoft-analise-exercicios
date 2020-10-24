def distancia(velocidade, teta):
    y = velocidade*velocidade*sin(2*teta))/9.8 + 2
    return y
velocidade = float(input('Qual a velocidade? '))
teta = float(input('Qual o angulo? '))
if distancia < 100:
    print('Muito perto')
if distancia > 100:
    print('Muito longe')
else:
    print('Acertou')