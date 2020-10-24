#raio de 2m
#100m = alvo
import math
g=9.8
v= int(input('Qual é a velocidade? '))
teta= int(input('Qual é o angulo que você deseja jogar? '))
d= ((v**2)*math.sin(2*teta))/g
if d > 97 and d < 103:
    print ('Acertou')
elif d > 102:
    print('Muito longe')
elif d < 98:
    print ('Muito perto')