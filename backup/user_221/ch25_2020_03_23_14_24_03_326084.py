velocidade = float(input('Qual a velocidade? '))
teta = float(input('Qual o angulo? '))
def d(velocidade, teta):
    y = (velocidade*velocidade*sin(2*teta))/9.8
    return y
if y < 100:
    print('Muito perto')
if y > 100:
    print('Muito longe')
else:
    print('Acertou')