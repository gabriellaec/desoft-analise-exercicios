import math 
v = int(input('Digite a velocidade: '))
teta = int(input('Digite o ângulo: '))

d = ((v**2) * math.sin(math.degrees(2*teta)))/ 9.8

if d < 98:
    print ('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')