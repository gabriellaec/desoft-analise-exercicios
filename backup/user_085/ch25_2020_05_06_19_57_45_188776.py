import math
v = float(input('Digite a velocidade de lançamento: '))
a = float(input('Digite o ângulo de lançamento: '))
d = ((v**2)* math.sin(2*(math.radians(a))))/9.8
if 98 <= d <= 102:
  print('Acertou!')
elif 98 > d:
  print('Muito perto')
else:
  print('Muito longe')