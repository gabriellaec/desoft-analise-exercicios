import math
v=int(input("Qual a velocidade de lançamento de sua jaca? "))
ang=int(input("Qual o angulo de lancamento de sua jaca? "))
d=(v**2*(math.sin(2*ang)))/9.8
if d<100:
    print('Muito perto')
elif d==100:
    print('Acertou!')
elif d>100:
    print('Muito longe')