import math
g = 9.8
v = int(input("Qual a velocidade da jaca: "))
O = int(input("Qual o angulo do lançamento: "))
d = ((v**2)*math.sin(2*O))/g

if d <= 102 and d >= 98:
    print('Acertou!')
elif d < 98:
    print('Muito perto')
else:
    print('Muito longe')